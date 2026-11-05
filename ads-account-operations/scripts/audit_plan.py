#!/usr/bin/env python3
"""Offline snapshot checks. No API calls, credentials or account mutations."""
import argparse
import json
import math
import re
import sys
import unicodedata


def normalize(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def literal_match(query, text, match_type):
    query, text = normalize(query), normalize(text)
    if not text:
        raise ValueError("Negative text must not be empty")
    if match_type == "exact":
        return query == text
    if match_type == "phrase":
        left = r"(?<![a-z0-9])" if text[0].isascii() and text[0].isalnum() else ""
        right = r"(?![a-z0-9])" if text[-1].isascii() and text[-1].isalnum() else ""
        return bool(re.search(left + re.escape(text) + right, query))
    if match_type == "broad":
        return set(text.split()) <= set(query.split())
    raise ValueError("Unknown match_type: " + match_type)


def index_unique(rows, name):
    result = {row["id"]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError("Duplicate " + name + " ID")
    return result


def amount(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Budget amounts must be numeric")
    if not math.isfinite(value) or value < 0:
        raise ValueError("Budget amounts must be finite and nonnegative")
    return value


def audit(snapshot):
    issues, checks = [], []
    if snapshot["snapshot_complete"] is not True:
        issues.append("Snapshot incomplete: check exports and attached shared lists")
    currency = snapshot["currency"]
    if not currency:
        raise ValueError("Currency is required; use one currency per snapshot")
    budgets = index_unique(snapshot["budgets"], "budget")
    campaigns = index_unique(snapshot["campaigns"], "campaign")
    groups = {}
    for campaign in campaigns.values():
        if campaign["status"] not in {"enabled", "paused", "removed"}:
            raise ValueError("Unknown campaign status")
        for group in campaign["ad_groups"]:
            key = (campaign["id"], group["id"])
            if key in groups:
                raise ValueError("Duplicate ad group ID within campaign")
            if group["status"] not in {"enabled", "paused", "removed"}:
                raise ValueError("Unknown ad group status")
            groups[key] = group
            if campaign["status"] == group["status"] == "enabled":
                if "approved_ads" not in group or group["approved_ads"] is None:
                    issues.append("Approved-ad status unknown for " + "/".join(key))
                elif isinstance(group["approved_ads"], bool) or not isinstance(group["approved_ads"], int) or group["approved_ads"] < 0:
                    raise ValueError("approved_ads must be a nonnegative integer or unknown")
                elif group["approved_ads"] == 0:
                    issues.append("Enabled group has no approved ads: " + "/".join(key))
    active_budgets = {c["budget_id"] for c in campaigns.values() if c["status"] == "enabled"}
    total = sum(amount(budgets[b]["daily_amount"]) for b in active_budgets)
    limit = amount(snapshot["daily_budget_limit"])
    if total > limit:
        issues.append(f"Active daily budgets {total:g} exceed planned {limit:g} {currency}")
    for negative in snapshot["negatives"]:
        campaign_id, group_id = negative["campaign_id"], negative.get("ad_group_id")
        if campaign_id not in campaigns or (group_id is not None and (campaign_id, group_id) not in groups):
            raise ValueError("Negative refers to an unknown campaign/ad group")
        literal_match("", negative["text"], negative["match_type"])
    active_groups = {key for key, group in groups.items()
                     if group["status"] == campaigns[key[0]]["status"] == "enabled"}
    checked_groups = {(case["campaign_id"], case["ad_group_id"]) for case in snapshot["routing_checks"]}
    for key in sorted(active_groups - checked_groups):
        issues.append("No routing cases supplied for active group: " + "/".join(key))
    for case in snapshot["routing_checks"]:
        key = (case["campaign_id"], case["ad_group_id"])
        group, campaign = groups[key], campaigns[key[0]]
        if case["expect"] not in {"allowed", "excluded"}:
            raise ValueError("Expected routing must be allowed or excluded")
        hits = [n["text"] for n in snapshot["negatives"]
                if n["campaign_id"] == key[0] and n.get("ad_group_id") in {None, key[1]}
                and literal_match(case["query"], n["text"], n["match_type"])]
        active = campaign["status"] == group["status"] == "enabled"
        passed = active and bool(hits) == (case["expect"] == "excluded")
        checks.append({**case, "active": active, "literal_negative_hits": hits, "passed": passed})
        if not passed:
            issues.append("Routing check failed: " + "/".join(key) + " query=" + case["query"])
    return {"active_daily_budget_total": total, "currency": currency, "issues": issues,
            "routing_checks": checks, "limitations": [
                "Literal negative checks only; not proof of keyword matching, auction eligibility or delivery.",
                "Broad matching uses whitespace tokens. Japanese segmentation and platform semantics are not simulated.",
                "Daily budget totals are planning amounts, not hard daily or monthly spend caps."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", help="Private normalized JSON snapshot; never committed by this tool")
    args = parser.parse_args()
    with open(args.snapshot, encoding="utf-8") as source:
        report = audit(json.load(source))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fictional behavioral scenarios. Does not contact an advertising platform."""
import copy
import unittest
from audit_plan import audit, literal_match


def fixture():
    return {"snapshot_complete": True, "currency": "USD", "daily_budget_limit": 100,
            "budgets": [{"id": "main-budget", "daily_amount": 90},
                        {"id": "legacy-budget", "daily_amount": 10}],
            "campaigns": [
                {"id": "main", "status": "enabled", "budget_id": "main-budget", "ad_groups": [
                    {"id": "core", "status": "enabled", "approved_ads": 2},
                    {"id": "nova", "status": "enabled", "approved_ads": 2}]},
                {"id": "legacy", "status": "enabled", "budget_id": "legacy-budget", "ad_groups": [
                    {"id": "classic", "status": "enabled", "approved_ads": 2}]}],
            "negatives": [
                {"campaign_id": "main", "ad_group_id": g, "text": "classic", "match_type": "phrase"}
                for g in ["core", "nova"]] + [
                {"campaign_id": "legacy", "text": "arbor", "match_type": "exact"}],
            "routing_checks": [
                {"campaign_id": "main", "ad_group_id": g, "query": "arbor classic", "expect": "excluded"}
                for g in ["core", "nova"]] + [
                {"campaign_id": "legacy", "ad_group_id": "classic", "query": "arbor", "expect": "excluded"},
                {"campaign_id": "legacy", "ad_group_id": "classic", "query": "arbor classic", "expect": "allowed"}]}


class SnapshotChecks(unittest.TestCase):
    def test_both_group_exclusions_are_sufficient_without_campaign_negative(self):
        self.assertEqual(audit(fixture())["issues"], [])

    def test_one_unprotected_group_is_detected(self):
        data = fixture()
        data["negatives"].pop(1)
        self.assertEqual(sum(not x["passed"] for x in audit(data)["routing_checks"]), 1)

    def test_campaign_inheritance_protects_both_groups(self):
        data = fixture()
        data["negatives"] = [{"campaign_id": "main", "text": "classic", "match_type": "phrase"},
                             data["negatives"][-1]]
        self.assertEqual(audit(data)["issues"], [])

    def test_reciprocal_rule_can_block_legacy_query(self):
        data = fixture()
        data["negatives"][-1]["match_type"] = "phrase"
        self.assertTrue(any(not x["passed"] for x in audit(data)["routing_checks"]))

    def test_active_budget_increase_detected(self):
        data = fixture()
        data["budgets"][0]["daily_amount"] = 100
        self.assertIn("exceed planned", audit(data)["issues"][0])

    def test_shared_budget_is_counted_once(self):
        data = fixture()
        data["campaigns"].append({"id": "additional", "status": "enabled", "budget_id": "main-budget", "ad_groups": []})
        self.assertEqual(audit(data)["active_daily_budget_total"], 100)

    def test_enabled_without_approved_ads_is_flagged(self):
        data = fixture()
        data["campaigns"][1]["ad_groups"][0]["approved_ads"] = 0
        self.assertIn("no approved ads", audit(data)["issues"][0])

    def test_unknown_approval_and_incomplete_snapshot_are_not_zero(self):
        data = fixture()
        del data["campaigns"][1]["ad_groups"][0]["approved_ads"]
        data["snapshot_complete"] = False
        result = audit(data)
        self.assertEqual(len(result["issues"]), 2)
        self.assertTrue(any("unknown" in x for x in result["issues"]))

    def test_phrase_respects_english_word_boundary_and_japanese_literal(self):
        self.assertFalse(literal_match("sweden cruise", "eden", "phrase"))
        self.assertTrue(literal_match("アルボル・クラシック", "クラシック", "phrase"))

    def test_invalid_reference_rejected(self):
        data = fixture()
        data["negatives"][0]["campaign_id"] = "wrong-account-campaign"
        with self.assertRaises(ValueError):
            audit(data)

    def test_unchecked_active_group_is_not_silently_certified(self):
        data = fixture()
        data["routing_checks"] = [x for x in data["routing_checks"] if x["ad_group_id"] != "nova"]
        self.assertTrue(any("No routing cases" in x for x in audit(data)["issues"]))

    def test_invalid_approved_ad_count_rejected(self):
        data = fixture()
        data["campaigns"][0]["ad_groups"][0]["approved_ads"] = -1
        with self.assertRaises(ValueError):
            audit(data)

    def test_paused_destination_is_not_reported_as_active_routing(self):
        data = copy.deepcopy(fixture())
        data["campaigns"][1]["status"] = "paused"
        self.assertEqual(sum(not x["passed"] for x in audit(data)["routing_checks"]), 2)


if __name__ == "__main__":
    unittest.main()

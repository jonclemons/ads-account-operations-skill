# Offline checks

`scripts/audit_plan.py` reads a normalized private JSON snapshot and writes a JSON report to standard output. It performs no network calls or mutations. Exit 0 means the supplied checks passed; exit 1 means issues were found. Invalid input raises an error rather than silently becoming zero.

Run:

```sh
python3 ads-account-operations/scripts/audit_plan.py /path/to/private-snapshot.json
python3 ads-account-operations/scripts/test_audit_plan.py
```

## Input contract

Use a fresh snapshot from one account/platform and currency. Keep its provenance and retrieval time in your private account manifest. The helper does not validate API freshness or translate platform exports. Normalize their fields explicitly:

```json
{
  "snapshot_complete": true,
  "currency": "USD",
  "daily_budget_limit": 100,
  "budgets": [{"id": "budget-a", "daily_amount": 100}],
  "campaigns": [{
    "id": "campaign-a", "status": "enabled", "budget_id": "budget-a",
    "ad_groups": [{"id": "core", "status": "enabled", "approved_ads": 2}]
  }],
  "negatives": [{
    "campaign_id": "campaign-a", "text": "unrelated", "match_type": "phrase"
  }],
  "routing_checks": [{
    "campaign_id": "campaign-a", "ad_group_id": "core",
    "query": "arbor unrelated", "expect": "excluded"
  }]
}
```

- IDs are strings. Status is `enabled`, `paused` or `removed`.
- `approved_ads` is a known nonnegative count; omit or use null when unknown. Zero flags an enabled group with no approved ads.
- `negatives` contains active entries only, with unwrapped text and `exact`, `phrase` or `broad`. Add `ad_group_id` for direct group entries; omit it for inherited campaign entries.
- Expand attached shared-list entries to each applicable campaign before checking. Set `snapshot_complete` false if contents/attachments are missing. Do not silently omit a list.
- Campaigns sharing a native budget must reference the same budget ID, so the amount is counted once. Supply all relevant active campaigns. This is a configured budget check, not actual spend forecasting.
- Add allowed and excluded query cases for every active group, especially during migration. `allowed` means no literal negative hit was found in the supplied rules; it does not assert positive keyword coverage or live serving.

## Limits

The helper uses NFKC/case/whitespace normalization only for comparisons; it does not modify submitted terms. Phrase matching uses literal text and English word boundaries. Broad matching is a whitespace-token approximation. Neither simulates Japanese tokenization, synonyms, punctuation rules, semantic matching or platform-specific matching behavior.

The script has no access to ads, match eligibility, account defaults or attached lists beyond the supplied snapshot. Preserve original strings and verify platform behavior separately. Never describe a passing result as certification that a live account is safe or delivering.

This is not an automatic negative sync. A live sync implementation should start with dry-run diffs, explicit managed ownership, verified API adapters and before/after checks. It must not delete unmanaged entries or infer permission to change an account.

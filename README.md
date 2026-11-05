# Ads Account Operations

A reusable Codex skill for Google Ads and Yahoo JP Search audits, keyword discovery, budget-separated migrations and concise reporting, with Meta, GA4 and Search Console workflows.

Includes the operator's preferences: intent-level analysis, qualified conversion efficiency, deliberate budget control, approval boundaries and concise reports without em dashes. No client data, account IDs, credentials or private reporting links are included.

## Use

Copy `ads-account-operations` into your Codex skills directory, then invoke:

```text
Use $ads-account-operations to audit this account. Check keyword-topic
performance, effective negatives, active budgets and ad eligibility. Report only.
```

```text
Use $ads-account-operations to propose brand keywords from this Search Console
export, checking existing paid coverage and reseller exclusions.
```

```text
Use $ads-account-operations to stage a legacy-product campaign within our
existing budget. Copy only its group and preserve approved ads and assets.
```

Provide the account's timezone, currency, budget, topic boundaries, conversion definitions and permissions. Newer user directions and account instructions override the included defaults. The skill does not grant access or authorize account changes.

## Contents

- `SKILL.md`: workflow selection and essential decision rules.
- `references/`: operator preferences, account operations, reporting/discovery and offline checks.
- `scripts/audit_plan.py`: dependency-free local checks of normalized budget/routing snapshots.
- `scripts/test_audit_plan.py`: fictional regression scenarios.

The live synchronization script is not implemented yet. A [separate implementation prompt](ads-account-operations/references/live-sync-prompt.md) defines its scope, API adapters, ownership controls and verification requirements.

See [offline checks](ads-account-operations/references/offline-checks.md) for the input format. The helper does not connect to an ad platform. Passing it does not prove live matching or serving.

## Privacy

Keep account manifests, exports, keys and reporting destinations in a separate private workspace. Approval and publishing permissions remain task-specific. Test fixtures use fictional data.

## Validate

```sh
python3 ads-account-operations/scripts/test_audit_plan.py
```

The skill uses available authenticated tools or native browser reports. It contains no SDK, credential setup or autonomous bidding system.

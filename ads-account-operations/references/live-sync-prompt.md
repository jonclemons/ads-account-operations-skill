# Prompt for implementing live negative synchronization

Use this in a separate coding conversation. Replace only the repository URL if using a fork.

```text
Implement a production-ready negative-keyword synchronization CLI in:
https://github.com/jonclemons/ads-account-operations-skill

Read the skill, references and existing offline checker first. Keep this a small,
maintainable tool, not a hosted service. Preserve unrelated repository work.

Goal: maintain private master rules for Google Ads and Yahoo JP Search, inspect
fresh live state, show a deterministic diff, and optionally apply authorized
changes. The current audit_plan.py is an offline checker, not a live sync.

Model three purposes separately:
1. Common irrelevant/partner exclusions shared by selected campaigns.
2. Campaign-specific routing exclusions separating brand/current/legacy/other
   product budgets. Never attach a topic's exclusion list to its own campaign.
3. Within-campaign routing as direct ad-group negatives. Native campaign shared
   lists are not linked ad-group lists; synchronize their entries explicitly.

Use stable platform/account/campaign/ad-group IDs. Keep client configuration,
credentials, exports, plans, ownership state and run logs private and gitignored.
Use fictional public examples. Preserve original Japanese text, spacing and
punctuation; comparison normalization must not silently rewrite submitted terms.

Verify current official API documentation for each adapter. Read all pages,
statuses, list contents and attachments. Apply platform-specific supported match
types. Missing permissions, incomplete state or unknown scope must stop a plan,
not be interpreted as empty. Do not ask users to paste credentials into chat.

Default to read-only dry-run. Emit additions, removals and association changes
with source rule, scope, match type and reason. Make output stable/idempotent.
Applying requires an explicit flag and a reviewed plan bound to the exact
account and live-state fingerprint. Abort on drift; never blindly overwrite.

Track ownership of objects created/explicitly adopted by this tool. Preserve
unmanaged negatives and shared-list associations. Do not delete lookalikes based
on text alone. Treat a shared-list edit as affecting every attached campaign,
including campaigns outside the current selection; show that impact before apply.
Never mutate an unapproved campaign/account through a shared list indirectly.

Use bounded batches and retries. Journal confirmed API results and partial
failures. A retry must not duplicate entities or repeat successful removals.
Save before-state and a reviewable recovery plan. Re-read live state after apply
and verify the intended diff; submitting an API request is not completion.
Never change positives, ads, pins, assets, budgets, bidding, goals or networks.

Extend meaningful tests for inheritance, all active groups already protected
without campaign-level copies, one unprotected group, mixed brand/legacy queries,
Japanese/English variants, duplicate rows, unsupported match types, shared lists
attached elsewhere, paused groups, ownership, pagination failure, drift, rate
limits, partial apply, idempotent reruns and rollback planning. Keep offline
literal matching clearly distinguished from actual platform eligibility.

First finish implementation, documentation and synthetic/mocked verification.
Do not deploy, schedule or mutate a live account without explicit authorization
in this conversation. If live access is unavailable, report the precise gap;
do not substitute mock success for live verification. Preserve a public repo
with no client information or credentials.

Deliver working code, a private-config template with fictional IDs, dry-run and
apply instructions, test results, documented API limitations, and a concise
summary of what is verified versus still pending. No em dashes in prose.
```

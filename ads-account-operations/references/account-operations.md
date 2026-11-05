# Account audits and campaign migrations

## Analysis

Use matching completed periods in account time. Refresh both periods for attribution lag. Record the actual dates and freshness. Use recent and longer periods when they materially inform a decision.

Map historical and current groups to stable keyword topics. A keyword moving between exact/phrase or groups must not appear as lost demand. Include historical activity from paused/removed entities. Reconcile topic totals to scoped campaign totals without adding total rows twice.

For each topic compare spend, impressions, clicks, all conversions, primary conversions, CPA and action mix. Calculate ratios from summed numerators and denominators, not averages of row percentages. Use native whole-period impression share; never average daily, keyword or campaign shares.

Distinguish volume, traffic composition, measurement and within-topic changes. Known PR ending or a future on-sale date is business context, not a new mystery. Assess competition using auction evidence, CPC and rank loss.

## Routing

Organize negatives by purpose. Shared general-irrelevance and partner lists can attach to the appropriate campaigns. Keep cross-campaign routing in campaign-specific lists or direct campaign entries, attached only to their intended destinations. Use direct ad-group negatives for routing within a campaign. Native shared negative lists do not become linked ad-group lists. A private master rule set can drive synchronization of those individual entries, but that requires an implemented, authorized sync mechanism. Do not claim this package already supplies live synchronization.

Build a query-to-destination matrix: bare brand, current product, legacy aliases, legacy plus price, product plus year, mixed current/legacy, partner plus brand, unrelated and support intent. Resolve mixed queries explicitly so reciprocal negatives do not block them everywhere.

For every active group, inspect the union of ad-group, campaign and attached shared-list exclusions. Record match type and scope. Absence at campaign level is not a defect if all active groups already have the required exclusions. Do not claim a gap after checking only one group or a filtered export.

Negative matching differs from positive matching and between platforms. Keep actual Japanese spellings, spaces, punctuation and aliases in evidence. Check current official documentation when behavior is uncertain. Positive exact close variants do not establish negative coverage.

Avoid broad brand-word exclusions that also block legitimate product/legacy combinations. Preserve the account's TA/reseller policy. New search observations do not authorize reversing partner exclusions.

Check proposed positives and negatives before import, then export saved state and repeat. Literal tests approximate matching; they do not certify auctions, live eligibility or conversion potential.

## Split and cutover

1. Privately snapshot source/destination entities and settings. Verify IDs and contents. Reuse a suitable clean shell.
2. Allocate within the approved combined envelope. Check every active campaign, count shared budgets once, and compare actual month-to-date spend with remaining allowance.
3. Copy only the intended group or populate its existing matching shell. Preserve approved text, pins, links and assets. An existing keyword shell may contain no ads.
4. Verify bidding/ceiling, Search Partners, Display, AI expansion, automatic text/URL changes, geographic presence, language, schedule, dates, tracking and conversion goals. Do not reset conversion definitions to accommodate a migration.
5. Preserve general and partner exclusions. Transfer applicable group routing rules; ensure the new campaign does not exclude its own topic.
6. Stage reciprocal routing and source pauses. Keep source coverage until replacements are eligible unless the user explicitly accepts an earlier switch. Distinguish enabled, approved and delivering.
7. At the authorized cutover, coordinate budgets, destination activation, source pause and routing in an order consistent with the user's coverage/budget tradeoff. Do not also change bidding repeatedly.
8. Read back all saved states. Confirm intended topic destinations, total active budgets, review status and unrelated campaigns' statuses. Retain a rollback using original entities.

A user-performed cutover calls for live verification, not replaying the plan. Report budget discrepancies, pending reviews and actual routing defects separately. Correct interim findings directly when complete evidence disproves them.

## Outputs

Proposals should identify platform, campaign/group, exact setting or keyword/match type, expected behavior and evidence. Do not promise a CPA outcome from a structural change.

Imports must use the platform's verified schema, consistent encoding and explicit statuses. Deduplicate conflicting rows. Exclude unapproved ad/asset edits. Read warnings before acceptance; do not ignore ambiguous entity matches.

Audits lead with actionable differences, scope/date and unverified checks. Keep account settings unchanged unless fixes are authorized separately.

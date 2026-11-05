# Reporting and query discovery

## Verified sources

Require successful status, retrieval after the expected scheduled refresh, expected dates/account and duplicate-free rows. A midnight validation run does not prove a daytime refresh succeeded. Delayed rows are pending, never zero. Append-only conversions may be stale; refresh comparison periods for attribution lag.

Keep definitions distinct:

| Metric | Required distinction |
| --- | --- |
| Search all conversions | Confirm the included action set |
| Search primary conversions | Confirm column and bidding-goal configuration |
| GA4 events | State event, attribution and source/dimension filters |
| Meta results | Use the exact action, such as Website Completed Registration |
| Search Console | Organic queries/pages, clicks, impressions, CTR and position |

Phone-link clicks are not completed calls; downloads are not unique prospects; partner clicks are not bookings. A generic feed column called Conversions may not be the requested result. Never sum unlike platform outcomes into a cross-channel conversion total.

For page rates, use the same page, period and appropriate session/user/event scope for numerator and denominator. Label diagnostic ratios when attribution scopes differ.

Daily: yesterday vs same weekday, rolling seven days vs prior seven. Weekly: use the established week boundary. Show actual MTD channel spend only when verified, then remaining allowance/days and pacing. Keep actual spend, budgets and forecasts separate. Reporting-only tasks do not repair feeds, edit documents or mutate accounts by implication.

## Creative and audiences

Compare latest/incumbent creatives over identical dates. Combine copies of the same creative, verifying identity. Generation/variant names do not establish experimental pairs. Inspect useful audience volume tiers with spend, requested results and CPA.

Recommend which ads to lead with and retain per audience. Delivery allocation is operational evidence, not randomized causal proof. Say "still too early to know" when new audiences lack evidence and label their first look preliminary.

## Search Console

Verify property, country, search type, latest complete dates and the preceding matching period. Do not claim a historical export is an API connection. Keep query and query/page exports separate to prevent double-counting. Absence from previous returned rows does not prove no prior searches.

Group variants by intent. Compare candidates with fresh positive keywords, negatives and matched paid queries on each platform. Distinguish missing explicit keywords from missing coverage through phrase/close variants. Do not add every punctuation/spacing variant just to reproduce an organic export.

Return a small ranked shortlist: query group, organic clicks/impressions/trend, recommended exact/phrase, destination, landing page, current coverage and exclusion conflicts. Separate additions, already-covered topics, watch lists, partner exclusions and paused other-product ideas. Brand-only scope does not authorize generic, competitor or foreign-market expansion.

Organic observations are not incremental paid-click forecasts or total market search volume. Search Console has no signup/booking counts. Do not invent query-level conversion joins to GA4 or Ads.

## Automation and slide output

Separate collectors, validated snapshots, calculations and presentation templates. Reuse authenticated helpers/secure properties; never copy or print keys. Respect original workbooks and use a separate destination when requested.

Upsert stable keys and refresh history for attribution lag. Verify reruns without duplicates. Track date coverage so incomplete periods do not look complete. Store IDs as text; preserve suppressed/unavailable values. Use native period impression shares. Retain lineage internally.

Retain all previously reported metrics in source tables; make concise one- or two-slide views. Bind numbers and commentary to the same reviewed period. Do not present old notes under new dates. Inspect the intended reference deck and render/read back the output before claiming completion.

Schedule recurring checks/emails only when requested. Local browser jobs require an available computer and authenticated session. Cloud independence exists only after permissions, live tests and schedules are verified. Avoid duplicate triggers, reports and completion notices. Do not promise an unfinished integration is live.

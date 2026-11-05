# Search strategy, creative and assets

Use with [account design](account-design.md) for Search education, planning and audits. All examples are fictional. Platform documentation was checked on 5 November 2026. Recheck changing controls and eligibility before an implementation. Some Yahoo help pages returned loading errors directly; their official indexed text supplied the guidance below.

## STAG and commercial boundaries

SKAG means single keyword ad group. STAG means single topic ad group, an operating convention rather than a platform campaign type. Group terms that deserve the same approved message and destination. Combine relevant exact/phrase and spelling variants for analysis without assuming their positive matching is literal. A new spelling alone rarely needs a new group.

For example, separate Nova exact, phrase and spacing groups can become one Nova topic group. Core brand remains a different topic when it needs a different page. A price query can stay in Nova if the same page answers it. A Classic-to-Nova query needs an explicit routing owner and a useful transition answer. Choose boundaries by search task and business economics.

| Search intent | Objective | Evaluate | Budget decision |
| --- | --- | --- | --- |
| Brand, such as `arbor nova` | Capture existing company/product interest | Relevant coverage, qualified actions, cost and value | Fund worthwhile capture, considering incrementality |
| Generic, such as `guided hiking tours` | Acquire category/problem demand | Qualified CPA, lead-to-sale rate, margin or value | Give acquisition a deliberate allocation when economics differ |

Keep brand and generic reporting distinct. A low brand CPA does not prove incremental sales or justify the same target for generic traffic. Brand interest may come from PR, sales, organic discovery and other media. A feasible holdout or geographic test can investigate incrementality.

Core plus current product can share Main initially. Legacy deserves a separate campaign when its own spending limit or objective is useful. Other products require approval. Separate budgets for meaningful economic decisions, not every keyword. Shared budgets do not reserve independent allocations. Daily budgets are not hard monthly caps. See [Google budgets](https://support.google.com/google-ads/answer/2375454?hl=en).

## Approved creative and assets

Build an asset inventory by topic, including approval, association, destination, status and eligibility. Preserve approved wording, pins and asset associations in migrations unless the user authorizes changes. An unchanged copy can still require association approval under the account contract. Review automated assets separately from uploaded ones.

- RSAs: cover topic, concrete benefit, proof and next step. Every combination should make sense. Avoid duplicate claims. Both platforms allow up to 15 headlines and 4 descriptions. Yahoo counts full-width characters differently, so check its native rules.
- Pin only necessary text, such as mandatory claims or disclaimers. Place required wording in a position guaranteed to appear under the applicable format. Existing approved pins take priority over optimization suggestions.
- Google currently recommends at least two Good/Excellent RSAs per group with distinct final URLs. Use genuinely relevant approved destinations. Do not create arbitrary pages or duplicates to satisfy a checklist. Yahoo currently recommends one RSA per group. Ad Strength is feedback, not Google Ad Rank or a serving guarantee.
- Sitelinks: useful alternative pages and descriptions. Google's asset guide says at least four active links, while its newer Ad Strength guidance asks for six or more relevant links. Aim for useful coverage without inventing weak destinations.
- Callouts: concrete benefits that add information. Structured snippets: factual categories under a suitable header. Avoid promotional claims in snippets.
- Business identity: verified, consistent business name and logo. Images: relevant, rights-cleared product/service visuals with suitable crops and platform eligibility. Consider square and landscape coverage.
- Conditional Google assets: calls when staffed and tracked, locations when a physical visit is useful, lead forms when eligible with consent, routing and qualified-lead measurement. Price, promotion or app assets can serve relevant objectives. Do not assume identical Yahoo options.

Sources: [Google RSA guidance](https://support.google.com/google-ads/answer/9921843?hl=en), [Google asset use cases](https://support.google.com/google-ads/answer/12073962?hl=en), [Google images and required-text positions](https://support.google.com/google-ads/answer/9566341?hl=en), [Yahoo RSA recommendation](https://ads-help.yahoo-net.jp/s/article/H000044220?language=en_US), [Yahoo input rules](https://ads-help.yahoo-net.jp/s/article/H000044241?language=en_US), [Yahoo pins](https://ads-help.yahoo-net.jp/s/article/H000044286?language=ja).

### Platform distinctions that affect approvals

Yahoo JP lists quicklinks, phone number, text supplements, category supplements, image, favicon and business-name assets. Verify eligible association scope for each type. Favicon uses campaign association, not ad-group association. [Yahoo assets](https://ads-help.yahoo-net.jp/s/article/H000045056?language=ja), [favicon scope](https://ads-help.yahoo-net.jp/s/article/H000054508?language=en_US).

Yahoo says automatic quicklink creation and association became enabled from 16 September 2026. Inspect this account control and system-created associations when approvals matter. Do not silently toggle it during an audit. [Yahoo asset automation](https://ads-help.yahoo-net.jp/s/article/H000065010?language=ja).

For focused brand capture, start with Google Search Partners, Display expansion and AI Max off, and Yahoo keywordless query matching off initially. Keep automatic text and final URL expansion off when approvals require fixed messages and destinations. Google warns URL expansion can bypass pinned assets. Audit separate dynamic asset settings too. Exceptions need an approved objective, spending control, query review and qualified outcome comparison. These are scope choices, not proof other inventory performs poorly. See [defaults and exceptions](account-design.md#inventory-and-automated-expansion).

## Evidence for creative and assets

Attribute any number with its metric, comparison, scope, period and original source. Label vendor averages. Do not add figures, predict account uplift, transfer Google results to Yahoo, or present associations as randomized causal estimates. No isolated uplift is asserted here for callouts, structured snippets, calls or lead forms.

| Vendor-reported average | Comparison and scope | Traceable source |
| --- | --- | --- |
| 15% more conversions | RSA plus sitelink Ad Strength moving from Poor to Excellent. Google internal data, 15 to 20 August 2025. Geography unspecified on the page. Combined creative claim, not isolated sitelink lift. | [Google Ad Strength](https://support.google.com/google-ads/answer/9921843?hl=en) |
| 8% more conversions at similar CPA | Search ads showing business name and logo, relative to the comparison without them implied by Google's wording. Global internal data, 9 to 22 March 2023. The help page gives no experimental design. | [Google asset guide, identity section and footnote](https://support.google.com/google-ads/answer/12073962?hl=en) |
| 6% higher CTR | Search ads when image assets show. Global internal data, 2 to 29 April 2023. The page does not specify assignment or experimental design. | [Google image assets](https://support.google.com/google-ads/answer/9566341?hl=en) |

These figures justify testing useful assets, not promising results. In a deck, place compact attribution beside each numeric claim and full source links plus caveats in notes. In the account, compare qualified results using a suitable test. Asset-level observed results reflect auction selection and are not automatically causal uplift.

## Measurement, discovery and migration

Report topics across old/new groups, match types and variants while retaining raw rows. Reconcile totals. Separate all conversions, primary actions, qualified leads and sales. Check action mix, reporting lag, attribution, dates, currency and timezone before interpreting CVR. A blended decline can reflect a changed topic mix.

Read brand impressions alongside impression share. Google impression share uses estimated eligible auctions. Eligibility changes with targeting, rules and rank, so high share can coexist with lower demand. Compare lost share from budget/rank and annotate known PR, launch and sales timing before suggesting competition. [Impression share](https://support.google.com/google-ads/answer/2497703?hl=en).

Search Console reveals organic query clues, not paid coverage or a complete demand census. Review brand/product aliases, prices and transitions by relevant property, date, country and device. Check existing paid terms and actual queries before adding keywords. Some terms are anonymized or omitted. A page improvement or exclusion may be a better response than a new keyword. [Performance report](https://support.google.com/webmasters/answer/7576553), [data limits](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive).

For an authorized migration: baseline privately, stage intended entities, verify approval/eligibility, switch within the combined budget, read back effective settings and observe actual queries and topic economics. Keep rollback entities. Preserve bidding during a structural move unless separately justified. [Operations](account-operations.md) retains the detailed workflow. The [offline checker](offline-checks.md) only evaluates supplied snapshots. Live negative synchronization is not implemented.

Useful extensions include approved message tests, task-specific sitelinks, relevant images, a transition landing page, qualified sales imports, brand incrementality and bounded inventory/discovery trials. Each needs a question, comparison, primary outcome and decision window. Early or non-randomized results should be described accurately.

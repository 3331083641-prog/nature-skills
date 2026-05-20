# Selection Rules

## Include

- Topics: 农业、农村、农产品、农业投入品、农业金融、农产品进出口、农产品国际贸易政策、农产品国际贸易协定、农业经济、农产品价格。
- Related keywords: agriculture, agricultural products, rural, fertilizer, seed, pesticide, feed, irrigation, farm credit, agricultural finance, import, export, trade, commodity prices, food prices, crop prices, trade policy, trade agreement.
- Regions: 东南亚优先，特别关注泰国、柬埔寨、印度尼西亚；include other regions only when directly relevant to agricultural trade with these markets or when the user specifies another market.
- Event types: 政策发布、贸易协定、进出口变化、关税/非关税措施、价格波动、产量/供应变化、农资供应、农业金融政策、农村经济政策、重大项目、市场准入、检疫规则、政府采购、灾害对农业生产或价格的影响。
- Regional policy cooperation: ASEAN-level food security, energy security, agricultural supply-chain cooperation, regional reserve mechanisms, trade facilitation, or implementation of ASEAN declarations/action plans may be included as policy consulting items even when specific trade volume is not available.
- Relevance threshold: The news subject must be a core participant in the event, not merely mentioned in passing.
- Timeliness: Include articles published within 26 hours before the collection anchor unless the user specifies another window. If the source shows only a calendar date and no time, include articles dated on the collection date or the previous natural calendar day.
- Duplicate window: Before final selection, remove news that appeared in generated reports from the previous 3 natural days unless the new article adds substantial new facts.

## Exclude

- Pure marketing copy without concrete news facts.
- Articles with no visible source, publish time, or verifiable event.
- Articles published earlier than 26 hours before the collection anchor when a specific time is available.
- Date-only articles older than the previous natural calendar day.
- News topics, events, or source URLs already used in the previous 3 natural days of generated reports, unless there is a material update.
- Duplicate reposts that add no new facts.
- Opinion, rumor, anonymous speculation, or stock-price-only commentary unless the user explicitly asks for that category.
- Items where the keyword appears only in tags, ads, recommendations, or unrelated sidebars.
- General politics, tourism, entertainment, crime, or finance news unless it clearly affects agriculture, rural areas, agricultural inputs, agricultural finance, agricultural prices, or agricultural trade.
- Pure inspection, visit, study tour, exploratory discussion, technology observation, or delegation activity unless it results in a signed agreement, implemented policy, confirmed procurement/export/import deal, market access change, investment launch, or other substantive trade or production action.
- Small local progress within a very large national program unless the item has clear independent significance for agricultural trade, prices, inputs, production capacity, rural finance, or market access.
- National-level or policy-framed stories that lack concrete data, implementation details, trade volume, price, procurement quantity, export/import value, affected market, or measurable scale.
- Small-scale agricultural activities, ceremonies, launches, or harvest events whose data show limited scope or weak representativeness, unless they directly indicate a broader national market trend or policy shift.
- Promotional campaigns, tasting events, media shows, local brand displays, or product-marketing activities whose practical reach is too small, even when they mention agriculture, rural producers, or geographical indications.
- Technical research, testing methods, laboratory tools, or operational process improvements that are mainly scientific or quality-control oriented rather than a concrete trade policy, market access decision, export/import action, or regulatory change.
- Very narrow product-category stories, including single niche seafood or specialty-product access updates, when the affected category has limited coverage and does not indicate a broader agricultural, food, fisheries, or trade-policy trend.

## Ranking

When several items match, prioritize:

1. Higher factual importance or business impact.
2. More authoritative source.
3. More recent publication time.
4. More complete details such as amount, parties, date, location, or official quote.

For final inclusion, prefer fewer stronger items over padding the report. Exclude loosely related public-health, storage, consumer-safety, or general administrative notices unless they directly affect agricultural production, prices, trade, market access, rural economy, agricultural finance, or agricultural inputs.

Do not include a story merely because it mentions agricultural modernization, cooperatives, rural areas, or food security. Require a concrete policy implementation, signed agreement, export/import behavior, procurement, measurable market effect, price change, input supply change, or production capacity impact.

For policy and trade consulting output, favor items with concrete data support: export/import quantity, shipment value, affected country or market, agreement size, tariff/quota, price movement, stock level, production volume, or procurement scale. If an item lacks data support, include it only when the policy action itself is clearly significant at national or cross-border level.

ASEAN-level food security or agricultural supply-chain policy cooperation is a valid exception to the data-support preference when it is tied to a named declaration, action plan, ministerial meeting, regional mechanism, or implementation agenda. Label it clearly as a regional policy cooperation development rather than a concrete trade result.

## Paging And Stop Rule

- For each source, start from the newest list page.
- Scroll down, click `Next`, or use `Load more` until article publish times fall outside the 26-hour window.
- If only dates are visible, continue until reaching articles older than the previous natural calendar day.
- If the list page mixes old and new items, inspect additional pages until there are no plausible in-window items left.
- Do not stop after the first screen unless all visible items are already older than the 26-hour window.
- Use the source site's local timezone when clear; otherwise state the timezone assumption in the final output.
- If a source page or article page cannot be opened, times out, blocks access, or lacks enough information after 5 total attempts, skip it for the current run and continue with other sources.
- Before skipping, try fallback discovery with `site:domain` search queries and open specific article pages from search results. Use this especially for AKP (`akp.gov.kh`) and sources whose homepage blocks script access.

## Three-Day Duplicate Filter

- Search the previous 3 natural days of generated `.docx` reports before finalizing selection.
- Compare by source URL, translated title, original title, named entities, product/crop, country, policy/agreement name, and core event.
- Treat syndicated reposts and follow-on coverage of the same facts as duplicates.
- Keep an item only when it adds material new information, such as updated trade value, new government action, new market access decision, new price data, or a new affected country.

## Saved User Preferences

Add confirmed user preferences here, such as preferred industries, blocked sources, required regions, or target publication tone.

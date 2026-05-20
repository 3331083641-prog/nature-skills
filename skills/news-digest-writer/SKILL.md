---
name: news-digest-writer
description: Collect news from specified webpages or source lists, select items matching configured topics and rules, and rewrite them into a fixed Chinese news稿 format with source links. Use when Codex needs to open news pages, monitor webpages, pick relevant news, summarize selected items, or produce structured Chinese news drafts from online sources.
---

# News Digest Writer

## Workflow

1. Read `references/source-list.md` when the user does not provide a specific URL or when recurring sources are needed.
2. Open each specified webpage with the best available browser or web tool.
3. Treat the run start time, login time, or user-provided collection time as the collection anchor.
4. Browse each source chronologically from newest to older. Scroll down, click pagination, or use "load more" until article publish times are older than 26 hours before the collection anchor. If a source lists only a calendar date without a specific time, allow the previous natural calendar day as the earliest acceptable date.
5. If a webpage cannot be opened, loads too slowly, blocks access, or lacks enough information to verify candidates, retry or use fallback discovery up to 5 total attempts. Fallback discovery includes `site:domain` search queries, opening specific article pages from search results, and trying AMP/mobile variants when available. If all 5 attempts fail, skip that webpage for the current run and continue with other sources.
6. Extract candidate items with title, URL, publisher/source, publish time, author if available, and body text or summary.
7. Before final selection, inspect available reports generated in the previous 3 natural days and remove repeated or substantially similar news topics.
8. Read `references/selection-rules.md` before selecting items.
9. Keep only items that satisfy the inclusion rules and do not hit the exclusion rules.
10. Prefer primary sources, official releases, filings, government pages, and reputable media. Use current publish dates and verify time-sensitive claims.
11. Read `references/article-template.md` before drafting.
12. Draft in the "印度、东盟农业政策跟踪" monitoring format from `references/article-template.md`. Preserve names, dates, numbers, locations, organizations, and source links.
13. When the user asks to run a report or output the result, create a Word `.docx` file matching the provided sample format unless the user explicitly asks for plain text only.

## Source Handling

- Use absolute dates such as `2026年5月13日`; avoid only `今天`, `昨日`, or `近期` unless the source itself is vague.
- Convert relative publish times such as `3 hours ago` or `yesterday` into absolute times using the collection anchor and the source site's timezone when available.
- If the article has a date but no specific time, accept articles from the collection date and the previous natural calendar day; for example, a May 13 run may include May 12 articles when no time is shown.
- Do not invent missing facts. If a key detail is unavailable, say it is not disclosed or not found in the source.
- Do not copy long passages from source articles. Summarize and rewrite in original wording.
- When multiple articles report the same event, use the most authoritative source as the lead source and list supporting sources separately.
- For paywalled or partially visible pages, use only visible facts unless another accessible source confirms the missing details.
- For inaccessible or incomplete webpages, retry or use fallback discovery up to 5 total attempts. After 5 failed attempts, abandon that webpage for the current run instead of blocking the whole report.
- Fallback discovery pattern: search `site:{domain} {country/source topic keywords} {date/month}` and open specific article URLs from search results. This is required for sources like AKP where the homepage may be difficult to fetch but article pages are searchable.

## Time Window And Paging

- Default valid window: 26 hours before the collection anchor through the collection anchor.
- Date-only fallback: when no publish time is visible after checking the article page, include articles dated on the collection date or the previous natural calendar day, and exclude older dated articles.
- Continue scrolling, loading more, or opening the next page while the visible articles may still include items inside the 26-hour window.
- Stop a source only after reaching articles whose publish times are clearly older than the 26-hour window, or after the source has no more older pages to load.
- If article cards do not show publish times, open likely relevant articles until their article pages confirm whether they are inside or outside the 26-hour window.
- Record the collection anchor in the final output when the user asks for a daily or time-windowed digest.

## Three-Day Duplicate Filter

- Before drafting, compare candidates against the generated reports from the previous 3 natural days when those files are available.
- Check recent `.docx` reports in the user's monitoring folders and the current workspace output folder.
- Filter out repeated news when the same event, policy, project, agreement, price movement, export/import result, or source URL has already appeared in those recent reports.
- Keep a later article only if it contains material new facts, such as updated figures, a new policy decision, a new country response, or a meaningful follow-up not covered before.

## Selection

Use `references/selection-rules.md` as the default filter. If the user gives new rules, treat them as higher priority for that run and mention any major conflict with the saved rules.

For each selected item, keep a short internal note with:

- Why it matched the rules
- Which source supports the core fact
- Any uncertainty or missing field
- Whether the item reflects substantive action, not just inspection, exploratory contact, or a small local installment of a broad national program
- What concrete data supports its significance, such as trade quantity, shipment value, market affected, price, stock, output, procurement scale, or policy implementation scope
- Whether an otherwise low-data item qualifies as ASEAN-level food security, energy security, agricultural supply-chain, reserve mechanism, or trade facilitation policy cooperation tied to a declaration, action plan, ministerial meeting, or regional mechanism

## Output

Use the fixed "印度、东盟农业政策跟踪" Word document format in `references/article-template.md` unless the user provides another template.

Before finalizing, check:

- Every factual claim is supported by a source.
- The selected news matches the topic and event rules.
- Exclude inspection-only or exploratory stories unless they produce a signed agreement, concrete procurement/export/import action, implemented policy, market access change, or measurable agricultural market impact.
- Exclude minor local progress inside a broad national program unless it has independent significance for agricultural trade, prices, inputs, production capacity, rural finance, or market access.
- Exclude items with weak data support or small activity scale when they do not represent a national policy shift, cross-border trade action, or measurable agricultural market impact.
- Exclude small-reach promotional activities, technical/laboratory process stories, and very narrow product-category access updates unless they clearly indicate a broader policy, trade, market-access, or measurable market trend.
- Include ASEAN-level food security, energy security, agricultural supply-chain, reserve mechanism, or trade facilitation policy cooperation when tied to a named declaration, action plan, meeting, or regional mechanism; title and body must present it as regional policy cooperation, not as a concrete trade result.
- Repeated or syndicated items are merged rather than duplicated.
- News already used in the previous 3 natural days is removed unless it adds substantial new facts.
- The tone is factual, concise, and publishable.
- Source links are included.
- Each item follows the sample style: title line, one dense rewritten paragraph ending with source/date in parentheses, and the original URL on the next line.
- Article body length is a high-priority quality rule, not a cosmetic preference. Each article body should normally land in the 330-380 Chinese character range, with about 350 Chinese characters as the target. Do not treat any draft below 320 Chinese characters as finished unless the source truly lacks additional verified facts after rechecking the article.
- Before accepting a short draft, add verified facts from the source where available: policy mechanism, responsible agency, product or market scope, trade quantity/value, price or stock data, implementation timeline, affected countries, stated rationale, and follow-up action. If a candidate cannot support at least about 320 Chinese characters of substantive, non-padded content, prefer dropping it rather than publishing a thin item.
- The hard maximum for each article body is 500 Chinese characters. After meeting the 330-380 target where possible, shorten any draft over 500 characters before generating the Word file.
- The final artifact is a `.docx` file when a report is being produced.
- The guide section must correspond one-to-one with final news titles: no numbering, each guide line is exactly the corresponding title plus `。`.
- Before creating the Word file, check and record each article body length. Revise any body below 320 Chinese characters by adding verified source details or replacing the item; aim for 330-380 characters, and revise any body over 500 Chinese characters down below the hard limit.
- Before creating the Word file, ensure titles emphasize the substantive trade or policy action, not courtesy language such as thanking, meeting, or discussing. For example, prefer `印尼首批对澳大利亚出口尿素装运出港` over `澳大利亚感谢印尼供应化肥`.
- Before creating the Word file, check terminology and names: use full official institution names on first mention, translate obscure English technical terms into clear Chinese policy/regulatory language, avoid unexplained raw English, and add necessary geographic qualifiers in titles for unfamiliar places.
- Use Chinese institution names in titles when available, and avoid raw English acronyms or organization names such as `Bulog`.
- Introduce or translate source acronyms before use. Prefer Chinese throughout for terms such as `食品供应和价格稳定计划`; do not leave unexplained forms such as `SPHP`.
- Explain non-universal source categories such as `一区`, `二区`, or `三区` by adding the covered regions or rewriting the sentence so readers understand the scope.
- Ensure every USD conversion keeps exactly two decimal places.
- The Word layout follows the user's final formatting rules: red centered bold main title, blue centered daily title, unnumbered guide title lines, one news item per page, first article starts after a page break, 1.5 line spacing, and justified article bodies with a two-character first-line indent.

## Optional Script

Use `scripts/extract_article.py` when a single URL needs quick article text extraction from static HTML. Browser tools may still be better for dynamic pages, login pages, complex layouts, or manual verification.

Use `scripts/extract_recent_report_items.py` to extract recent report titles and URLs for the 3-day duplicate filter.

Use `scripts/create_digest_docx.py` to generate the final Word document from a JSON report payload.

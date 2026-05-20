# Article Template

Use this template for the user's "印度、东盟农业政策跟踪" daily monitoring drafts. The default final output is a Word `.docx` file. The structure is based on the provided Word samples from 2026年4月29日 to 2026年5月12日.

## Document Header

```text
印度、东盟农业政策跟踪
总第{issue_number}期
华南农业大学经济管理学院                          {yyyy.m.d}
{yyyy年m月d日}印度、东盟农业政策动态
【本期导读】
{导读1}
{导读2}
```

- Use the collection/report date in both date positions.
- Use `总第{issue_number}期` only when the issue number is known or provided. If unknown, ask the user or leave a placeholder.
- Keep `华南农业大学经济管理学院` in the header unless the user provides another unit.
- The guide section must correspond one-to-one with the final news items. Each guide line should be the exact final news title plus `。`.

## News Item Format

For each selected news item, write:

```text
{新闻标题}
近日，{主体/机构}表示/数据显示/发布/宣布，{核心事实}。{背景、数字、原因、影响和后续安排}。（{中文来源名}，{m月d日}）
{source_url}
```

- Place each news title on its own line.
- Put the full rewritten article in one dense paragraph after the title.
- Put the source name and date at the end of the paragraph in Chinese parentheses, then put the URL on the next line.
- Use the source Chinese names from `source-list.md`: 曼谷邮报、泰国国家报、高棉时报、安塔拉新闻社.
- If the source date is not visible, omit the date in parentheses only when it cannot be verified.
- Do not add labels such as `【正文】`, `【信息来源】`, `摘要`, or `影响分析` inside the final draft unless the user asks for a different format.

## Title Style

- Write a concise declarative Chinese title, usually 16-28 Chinese characters.
- Write titles for an international agricultural trade and policy briefing, not as general news headlines.
- Capture the substantive trade or policy action in the title, especially phrases such as `首批出口`, `装运出港`, `签署协议`, `批准协定`, `开放市场准入`, `启动采购`, `进口配额`, `出口限制`, `价格上涨`, or `供应短缺`.
- Avoid courtesy, diplomatic, or public-relations angles such as `感谢`, `会见`, `强调`, `表示`, or `讨论` when a concrete trade action is available.
- Do not use raw English organization names or acronyms in titles when a clear Chinese name exists. For example, write `印度尼西亚国家物流署将在2026年投放82.8万吨稳价大米`, not `印尼Bulog全年投放82.8万吨稳价大米`.
- Prefer the pattern `{国家/主体}+{关键贸易/政策动作}+{产品/市场}`.
- Add essential location qualifiers in titles when the place may be unfamiliar to the target reader. For example, write `中国磨憨口岸前四月进口鲜榴莲12.1万吨`, not only `磨憨口岸前四月进口鲜榴莲12.1万吨`.
- Use goal-oriented title wording when appropriate, such as `以冲刺...目标`, to clarify that a policy action supports an export or trade target.
- Examples of acceptable shapes:
  - `泰国加大榴莲等水果推广力度，力争出口额较去年增长5%`
  - `印尼将推动棕榈油产品满足《欧盟零毁林法案》认证`
  - `霍尔木兹海峡危机推高尿素价格并冲击亚洲粮食安全`

## Paragraph Style

- Start most articles with `近日，`.
- Body length is a high-priority content-quality rule. Use one long integrated paragraph per item, normally 330-380 Chinese characters, with about 350 Chinese characters as the target.
- A body below 320 Chinese characters is not acceptable as a finished item unless the source truly lacks additional verified facts after rechecking. First add substantive details from the source: policy mechanism, responsible agency, product or market scope, trade quantity/value, price or stock data, implementation timeline, affected countries, stated rationale, and follow-up action.
- Do not pad with vague background, generic importance, repetition, or unsupported analysis just to hit the target. If the source cannot support about 320 Chinese characters of substantive content, replace or drop the item.
- The hard maximum is 500 Chinese characters for each article body. First satisfy the 330-380 target where possible, then shorten any paragraph over 500 characters before generating the Word file.
- Include concrete numbers, dates, agencies, countries, products, prices, export/import amounts, policy names, and affected markets when available.
- Sequence the paragraph as: event lead, key data, reason/background, market or policy impact, follow-up action or broader implication.
- Keep tone neutral, factual, and research-monitoring oriented.
- Avoid unsupported dramatic words such as `重磅`, `爆发`, `颠覆`, `史诗级`, `遥遥领先`.
- Translate English source facts into natural simplified Chinese; do not preserve awkward source syntax.
- Translate obscure professional English terms into generally understandable Chinese policy or regulatory language. Avoid leaving raw technical English in the final text unless the exact term is necessary and can be explained naturally.
- Translate or introduce source acronyms before use. Prefer the Chinese policy or institution name throughout when it is clear; if an acronym is necessary, write the Chinese name first and put the acronym in parentheses on first mention. Do not use unexplained forms such as `SPHP` or `Bulog`.
- Explain non-universal administrative or pricing categories on first mention. If a source uses labels such as `一区`, `二区`, or `三区`, add the covered places in parentheses or rewrite the sentence so readers understand the geographic scope.
- Do not mistranslate technical systems or terms. If a term is unclear, use a broader accurate expression such as `通关制度`, `检验检疫制度`, `出口认证制度`, `追溯系统`, or `相关法规`, based on source context.
- Use full official institution names on first mention, such as `泰国农业与合作社部`; do not shorten to `农业部` if the country has a more specific official ministry name. After first mention, use `该部门`, `泰方`, or the full name again.
- Translate all personal names into Chinese. On first mention, use the Chinese transliteration and include the original English name only when needed for disambiguation.
- Convert every non-USD currency amount into USD immediately after the original amount, using the form `xxxx越南盾（约合xx美元）`, `xxxx泰铢（约合xx美元）`, or the relevant currency name. If an exchange rate must be looked up, use a current reliable rate and keep the conversion approximate.
- Converted USD amounts must keep exactly two decimal places. For large amounts, use natural Chinese units such as `万美元` or `亿美元`, also with exactly two decimal places when a decimal is shown.
- Preserve integer data as integers when the source gives integers, including dates, months, years, days, numbers of vessels, people, provinces, policies, containers, animals, and tonnes.
- Do not add meaningless `.00` to source figures that are integers. Only keep decimals when the original figure has decimals, when rounding is needed, or when presenting currency conversions.
- Do not over-precision copied percentages or amounts; for example, write `3.82%`, `0.19%`, `约合6.38亿美元`, or `约合1.20美元`, but write `220万吨`, `700万吨`, `3个月`, and `1582艘`.

## Guide Sentence Style

- Each guide sentence must match the corresponding news title exactly, followed by `。`.
- Do not number guide sentences in the Word output.
- End each guide sentence with `。`.

## Final Checks

- The header date, source date, and article facts are consistent.
- The number of guide lines equals the number of news items, and each guide line matches its corresponding news title.
- Every selected item has a title, one paragraph, and a source URL.
- The paragraph ends with `（来源名， m月d日）` or `（来源名）` before the URL.
- There are no bullet lists in the article body.
- The output keeps only relevant agriculture, rural, agricultural product, input, finance, price, import/export, or trade-policy content.
- Every currency amount includes an immediate USD conversion unless it is already denominated in USD.
- Every USD conversion keeps exactly two decimal places, such as `约合4.01亿美元` or `约合5.59美元`.
- Specialized English words and official terms are translated into clear Chinese, or replaced with a broader accurate policy/regulatory expression when the literal term would be obscure.
- Acronyms and source shorthand are translated or introduced before use; the final body must not contain unexplained abbreviations.
- Non-universal labels such as price zones, administrative groupings, program tiers, or source-specific categories are explained with their geographic or policy scope on first mention.
- Official institution names are complete on first mention and not casually shortened.
- Titles use Chinese institution names when available and avoid raw English acronyms or organization names.
- Titles include necessary geographic qualifiers for ports, cities, provinces, or border crossings that readers may not recognize.
- Personal names are written in Chinese.
- Numbers are rounded to two decimal places where rounding is appropriate.
- Integers from the source are not padded with `.00`.
- Each article body should normally be 330-380 Chinese characters, targeting about 350, and must not exceed 500 Chinese characters. Before Word generation, record the character count of every body; any body below 320 Chinese characters must be expanded with verified source details, replaced with a stronger item, or explicitly justified as source-limited.

## Word Output

- Generate a `.docx` file by default for finished reports.
- Use `scripts/create_digest_docx.py` with a JSON payload containing `issue_number`, `date_text`, `date_short`, `guide`, and `items`.
- Match the sample layout:
  - Main title: `印度、东盟农业政策跟踪`, centered, bold, dark red, 36 pt.
  - Issue line: centered, bold, 16 pt.
  - Unit/date line: unit bold and left aligned, date bold and right aligned, 14 pt.
  - Daily title: centered, bold, blue, 16 pt.
  - `【本期导读】`: bold, 14 pt.
  - Guide lines: unnumbered title lines matching final item titles, 12 pt.
  - Start the first article on a new page after the guide section.
  - Put each article on its own page.
  - Item titles: centered, bold, 14 pt.
  - Item body: 12 pt, justified, one dense paragraph with first-line indent of about 2 Chinese characters.
  - URL: separate line after each item, aligned with body indentation.
  - Line spacing: 1.5 for the whole document.

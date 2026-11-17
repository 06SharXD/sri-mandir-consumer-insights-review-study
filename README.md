# Sri Mandir Public Review Analysis & Consumer Insights

This repository contains a small, manually coded analysis of publicly accessible Sri Mandir app-store reviews. It is public-review analysis, not structured user interviews or a representative customer study. No private calls, fabricated testimonials, or invented review records are included.

## Contents
- `data/reviews.csv` — source-linked review register, including access date, dates as displayed, short excerpts, paraphrases, coding and confidence. Ratings are blank where the public page did not reliably expose an individual score.
- `data/codebook.md` — coding rules and category definitions.
- `analysis/analyze.py` — reproducible summary tables and charts.
- `analysis/outputs/` — generated CSV summaries and PNG charts.
- `workbook/review_tracker.xlsx` — review tracker and pivot-ready category and sentiment summaries.
- `report/insights_report.md` — findings, implications and limitations.
- `slides/consumer_insights_brief.pptx` — short presentation.
- `research/interview_guide.md` — guide for future real calls; no calls have been conducted.
- `project_jd_alignment_prompt.xml` — role-alignment prompt grounded in verified project evidence and limitations.

## Scope and method
The corpus contains **10 accessible review records** from Apple App Store review pages for Sri Mandir. Collection was checked on 2026-11-18. Each row is one distinct review visible in the source page; duplicated page rendering of the same review was not counted twice. Excerpts are kept short and the remainder is paraphrased. A primary category, sentiment or request intent, and confidence label were assigned manually. The record-level source URL points to the public review listing.

This is a convenience sample of surfaced English-language reviews on two regional Apple storefronts. It is not a complete export, random sample, or longitudinal panel. The date is retained as displayed, with ISO date populated only when the year is explicit. The storefront text did not reliably expose each review's star score in the extracted page content, so individual ratings are left blank rather than inferred. The findings describe these records only and cannot establish prevalence, causality, or representativeness.

## Reproduce
From the repository root, run:

```bash
python analysis/analyze.py
```

Install dependencies listed in `requirements.txt` first. The script reads `data/reviews.csv` and writes summary CSVs and PNG charts under `analysis/outputs/`.

## Public sources
- [Apple App Store Sri Mandir reviews, US storefront](https://apps.apple.com/us/app/sri-mandir-puja-chadhava/id1637621461?platform=iphone&see-all=reviews)
- [Apple App Store Sri Mandir reviews, India storefront](https://apps.apple.com/in/app/sri-mandir-puja-chadhava/id1637621461?platform=iphone&see-all=reviews)
- [Google Play Sri Mandir app listing](https://play.google.com/store/apps/details?id=com.mandir) — consulted for app identity and public aggregate context; not included in the coded corpus because individual review-level records could not be consistently captured and verified here.




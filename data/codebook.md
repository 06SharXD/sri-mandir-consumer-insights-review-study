# Codebook

## Unit and source
One distinct review displayed on the public Sri Mandir Apple App Store listing. Duplicate rendering of the same review is excluded. Access date is 2026-11-18. Individual star ratings are blank if not reliably available in the listing text.

## Fields
- `short_excerpt`: a short verbatim fragment, retained only to anchor the coded interpretation.
- `paraphrased_summary`: analyst paraphrase, not a quote.
- `primary_category`: one best-fit theme per record; secondary issues may be mentioned in the paraphrase but not counted as a second record.
- `sentiment_or_intent`: Positive, Negative, or Request. Requests are feature/service asks without an explicit overall evaluation.
- `coding_confidence`: High when the review directly states the theme; Medium when the year/date or meaning is ambiguous or a multi-issue comment needs interpretation; Low would indicate a weak inference.
- `review_date_as_displayed`: original visible text; `review_date_iso` only when a full year is shown.

## Categories
- Language and accessibility: language availability or ability to understand content.
- Content choice and personalization: deity/content selection tailored to the user's preference.
- Login and account access: authentication, sessions, account setup.
- Ritual convenience and service visibility: reminders, asynchronous access, evidence or visibility around a service.
- Temple discovery and information: locating a temple or its details.
- Service fulfilment and trust: perceived gap between paid promise and delivered service or follow-up.
- Ease of use and devotional connection: usability and perceived cultural/spiritual value.
- Ritual accuracy and personalization: correctness of devotee-specific ritual details.
- Booking reliability and cross-platform consistency: duplicate prevention and parity across app/web.

## Coding cautions
Code themes in the text, not user motives. A single review can mention more than one issue; the primary category captures its clearest actionable issue. Sentiment is expressed review intent, not an objective verdict on service quality. Counts are descriptive and must not be generalized to all users.
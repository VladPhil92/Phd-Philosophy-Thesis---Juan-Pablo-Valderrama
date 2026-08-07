# Library Methodology

## Epistemological layers

| Level | Layer | Rule |
|---:|---|---|
| 0 | Original source | Printed/digital edition, article, or official decision is bibliographic authority. |
| 1 | Machine transcription | OCR/extraction is probabilistic and non-authoritative. |
| 2 | Verified transcription | Human-reviewed text, always with explicit status and scope. |
| 3 | Human research notes | Juan Pablo's interpretations, questions, distinctions, and objections; never inserted into transcription. |
| 4 | AI-assisted research | Searches, comparisons, maps, summaries, objections, and candidate connections; assistance, not evidence. |
| 5 | Authorial argument | A claim accepted, reformulated, and intellectually assumed by the researcher. |
| 6 | Dissertation | Final prose for which the researcher assumes responsibility. |

No operation may collapse levels. Movement is recorded as:

```text
SOURCE_ID → SOURCE_PAGE → TRANSCRIPTION_PASSAGE → NOTE_ID → CONCEPT_ID
→ ARGUMENT_ID → CHAPTER_ID → DISSERTATION_CLAIM
```

Markdown links and YAML fields are sufficient. Example IDs: `SRC-DERRIDA-ANIMAL-FR`, `NOTE-DERRIDA-0042`, `CONCEPT-REACTION-RESPONSE`, `ARG-CH5-003`, `CHAPTER-05`. Existing argument/chapter records should link back to these IDs; a link is not verification.

## Authority and anachronism

`SOURCE CLAIM`, `RESEARCHER APPLICATION`, and `AI-SUGGESTED CONNECTION` must be separate headings/fields. Never write that Derrida predicted AI unless an original source explicitly establishes that claim. Applying iterability or sovereignty to computation is a researcher application, not retroactive attribution.

The AI may locate, compare, question, suggest, and criticize. **Juan Pablo Valderrama Pino determines the philosophical interpretation and assumes responsibility for the dissertation argument.**

## Corpus queries

Good: “Locate verified or partially verified Derrida passages on reaction/response; return source ID, original pages, context, status, and chapters; invent no quotation.”

Good: “Compare sovereignty occurrences in *La bête et le souverain* with computational sovereignty, separating textual evidence from researcher inference.”

Good: “Locate iterability in *Signature événement contexte*; label any AI relationship as researcher hypothesis.”

Bad: “Tell me what Derrida thinks about AI.” It invites anachronism, erases the source/application distinction, and encourages unsupported attribution.

## Quotation register

Each quotation record must give `quote_id`, `source_id`, exact edition, source page, language, verification status, context, related concepts, and proposed chapter. AI-located wording cannot enter the quotation register until a human compares it with the original. Markdown line numbers are never source pages.

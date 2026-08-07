# OCR Protocol

> OCR is a probabilistic transcription process. **OCR MATCH ≠ VERIFIED QUOTATION.**

## Pipeline

1. Ingest a legally obtained scan without altering it.
2. Identify all languages (Spanish, French, German, English, Greek as applicable).
3. Preserve the original in the private/local layer.
4. calculate SHA-256 (`sha256sum <file>`) and record it in `SOURCE-HASH.md`.
5. Run a documented engine appropriate to the source.
6. Preserve immutable initial output as `raw-ocr.md`.
7. Detect page boundaries and insert `<!-- SOURCE_PAGE: 127 -->` markers.
8. Remove scanner artifacts only through documented rules.
9. Reconstruct paragraphs while logging mechanical normalization.
10. Preserve footnotes/endnotes separately from body text.
11. Retain recoverable original pagination.
12. Audit names, accents, negations, Greek/German/French, and philosophical terms.
13. Generate `full-text.md`; never overwrite raw OCR.
14. Assign a scoped verification status.
15. Build an AI navigation index only from existing page markers.
16. Verify every dissertation quotation against the original edition.

No engine is mandatory: OCRmyPDF, Tesseract, PyMuPDF, `pdftotext`, multimodal OCR, or later tools may be used. Record software/version/configuration and transformations in the log.

## Canonical markers

```markdown
<!-- SOURCE_PAGE: 127 -->
<!-- OCR_WARNING: unreadable word, source page 73 -->
<!-- TERMINOLOGY_VERIFY: "différance", source page 91 -->
<!-- FOOTNOTE_VERIFY: source page 112 -->
<!-- PAGE_BOUNDARY_UNCERTAIN -->
```

Page markers are HTML comments so reading flow is uninterrupted. Do not fabricate a page number. Uncertain notes may use `[FOOTNOTE OCR UNCERTAIN — VERIFY SOURCE PAGE 87]`; reliable notes use Markdown footnotes. Never silently merge notes into body text.

## Cleanup constraints

Repeated headers, titles, author names, and scanner artifacts may be removed only by logged rules. Join line-break hyphenation only as a recorded mechanical normalization; preserve significant hyphenation. Never probabilistically “correct” technical terms. Preserve source language; translations are separate notes or separately identified bibliographic sources. Prefer semantic source divisions over arbitrary page chunks.

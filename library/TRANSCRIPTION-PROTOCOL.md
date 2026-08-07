# Transcription Protocol

1. Keep the private original immutable and hash-addressed.
2. Keep `raw-ocr.md` immutable after capture; corrections go to `full-text.md` and `corrections.md`.
3. Put `<!-- SOURCE_PAGE: n -->` before text from each original page. Printed pagination, not PDF viewer index or Markdown lines, controls `n`; document exceptions.
4. Preserve source language and meaningful typography. Put researcher translations in notes, never the transcription.
5. Preserve footnotes using `[^n]`; flag uncertain reconstruction rather than guessing.
6. Log cleanup, paragraph reconstruction, header removal, dehyphenation, accent restoration, and term changes in `TRANSFORMATION-LOG.md`.
7. Divide `sections/` according to the work's semantic structure. Computational retrieval chunks belong outside the human transcription.
8. Keep human notes and AI outputs in their own directories.

The cleaned file remains a research instrument, regardless of status. `SOURCE_LOCKED` freezes a verified derivative; it does not replace the edition as authority.

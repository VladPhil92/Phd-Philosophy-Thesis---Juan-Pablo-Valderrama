# Copyright and Distribution Policy

## Two-layer design

```text
PUBLIC RESEARCH REPOSITORY + PRIVATE / LOCAL SOURCE LIBRARY
```

The public repository may hold metadata, bibliography, hashes, page references, verification/provenance records, researcher-authored notes and analysis, conceptual indexes, AI interaction records, and limited quotations appropriate to scholarship. It must not automatically publish copyrighted books, scans, or full OCR derivatives.

The private/local layer may hold legally acquired PDFs, scans, ebooks, and working OCR. Stable `source_id` values connect it to public records without disclosure. `private_source_available: true` does not authorize distribution; `public_full_text_available: false` is the default pending verification.

Repository `.gitignore` excludes common source formats, private directories, and explicitly private transcription filenames. Before commit, run `git status` and a file-extension/private-path audit. Do not ignore `notes/`. Public-domain/licensed full text requires documented permission/status in `SOURCE.md` before inclusion.

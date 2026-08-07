# Source Verification Protocol

## Scoped transcription statuses

- `OCR_RAW`: untouched extraction.
- `OCR_CLEANED`: mechanically/structurally cleaned, not source-checked.
- `PARTIALLY_VERIFIED`: stated pages/passages checked by a human.
- `TERMINOLOGY_VERIFIED`: defined terminology audit completed; not whole-text verification.
- `FULLY_VERIFIED`: entire transcription compared page by page; reviewer and date required.
- `SOURCE_LOCKED`: verified derivative frozen by hash/version after review.

Never report merely “verified”; state status, reviewer, date, scope, exceptions, and original edition. AI confidence states are separate: `LOCATED`, `TRANSCRIPTION_MATCH`, `SOURCE_VERIFIED`, `INTERPRETATION_PENDING`, `INTERPRETATION_APPROVED`.

## Human citation gate

`READY_FOR_DISSERTATION = true` only if all are `yes`:

```text
source identified = yes
edition verified = yes
source page identified = yes
original checked = yes
quotation checked = yes
context checked = yes
researcher interpretation approved = yes
```

Any `no`, unknown, or TODO makes it false. A source-verified quotation can still have interpretation pending.

## Terminology audit

Manually check significant terms and every uncertain original Greek character. Minimum watch lists include Derrida: *différance, trace, supplément, itérabilité, arrivant, hospitalité, souveraineté, carnophallogocentrisme*; Heidegger: *Sein, Seiendes, Dasein, Mitsein, Welt, Gestell, Bestand*; Agamben: *homo sacer, zoē, bios, oikonomia*; Greek/transliterated: *logos, zoon, polis, zoon logon echon*. Record page, OCR form, original form, reviewer, date, and resolution; never silently replace a term.

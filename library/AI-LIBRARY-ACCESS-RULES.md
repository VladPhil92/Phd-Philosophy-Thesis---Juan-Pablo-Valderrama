# AI Library Access Rules

Every AI agent must:

1. report stable source ID;
2. report original page markers when available;
3. report scoped transcription verification status;
4. never invent missing text or pages;
5. never silently repair uncertain OCR;
6. separate quotation/source claim, researcher interpretation, and AI suggestion;
7. never treat summaries or OCR as evidence;
8. attribute an author only where source text supports it;
9. flag anachronism and unsupported contemporary application;
10. require original-edition checking before dissertation use.

AI may search, compare, count terms, identify candidates, map concepts, generate questions/objections, and assist navigation. It may not promote `TRANSCRIPTION_MATCH` to `SOURCE_VERIFIED`, invent page references, or mark an interpretation approved.

## Model output

```markdown
## Candidate passage

Source: SRC-DERRIDA-ANIMAL-FR
Work: L'animal que donc je suis
Source pages: 127–129
Transcription status: PARTIALLY_VERIFIED
Relevant concept: reaction / response
Corpus finding: The passage appears relevant to the distinction under investigation.
Research interpretation: Possible connection with Chapter 5's analysis of computational response.
Status: INTERPRETATION_PENDING
Required next action: Verify the passage against the original edition before quotation or dissertation citation.
```

The example demonstrates format only; its pages are not a populated index entry. **Juan Pablo Valderrama Pino determines interpretation and assumes responsibility for the dissertation argument.**

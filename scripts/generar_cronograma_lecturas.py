#!/usr/bin/env python3
"""Genera research/reading-schedule.md a partir de las obras registradas en
research/sources/library-manifest.md, en el orden metodologico fijado por
research/methodology.md (DEC-013, DEC-014).

Este script no verifica ni cambia el estado de ninguna fuente en el
manifiesto: solo secuencia en el tiempo obras ya registradas alli, con una
fecha de inicio y una regla de ritmo declaradas explicitamente. La regla de
ritmo es una estimacion de esta sesion, no una decision metodologica; puede
ajustarse editando la funcion peso() y volviendo a ejecutar el script.

Uso: python3 scripts/generar_cronograma_lecturas.py
"""
import datetime

START = datetime.date(2026, 8, 15)
OUTPUT_PATH = "research/reading-schedule.md"

HEADER = """# Cronograma de lecturas

**Estado: PROPUESTA, no decisión metodológica cerrada.** Este documento
secuencia en el tiempo las obras registradas en
[`research/sources/library-manifest.md`](sources/library-manifest.md);
no decide nada que `research/methodology.md` no haya decidido ya, y no
sustituye la sección de ese manifiesto que marca la "Lectura de primera
ronda" (`PRIORIDAD: ALTA`) como "propuesta, no decisión cerrada". El
investigador puede reordenar, fusionar, saltar o extender cualquier
tramo sin que eso implique reabrir ninguna decisión de
`governance/decision-log.md`.

**Fecha de inicio:** 15 de agosto de 2026.

Generado por [`scripts/generar_cronograma_lecturas.py`](../scripts/generar_cronograma_lecturas.py).
Para ajustar el ritmo de lectura, edita la función `peso()` de ese script y
vuelve a ejecutarlo; no requiere reescribir la secuencia de fases a mano.

## Qué fija este documento y qué no

- **Orden metodológico (sí fijado por decisión previa):** la secuencia de
  fases sigue directamente `research/methodology.md` §1–2 (`DEC-013`,
  `DEC-014`) — Derrida como fuente del método, luego los diez
  autores/pares que `DEC-013` nombra explícitamente como objeto de la
  lectura deconstructiva, en el orden exacto en que los enumera, y
  después el resto del corpus agrupado por la clasificación funcional ya
  existente en el manifiesto (A–I). No es una reclasificación nueva:
  reutiliza las categorías y prioridades (`ALTA`/`MEDIA`/`BAJA`) que el
  manifiesto ya declara.
- **Ritmo semanal (no fijado, es una estimación de esta sesión):** un
  libro ocupa 1 semana; los libros `ALTA` prioridad de las Fases 0–2
  (herramientas metodológicas, Derrida, y las diez genealogías
  nucleares) ocupan 2 semanas, para permitir relectura y fichaje más
  profundo; un artículo o capítulo corto ocupa 0.5 semana; `SRC-218`
  (dos obras en una fila) ocupa 2 semanas. **El investigador no ha
  fijado ningún ritmo de lectura real** — ni horas semanales
  disponibles, ni pausas, ni ritmo distinto por temporada académica.
- **Este cronograma no acredita lectura.** Que una obra tenga fecha
  asignada aquí no cambia su estado en `library-manifest.md`
  (`CANDIDATE` / `IDENTITY_VERIFIED`). El registro de lectura real sigue
  el procedimiento de `research/methodology.md` §4 (DEC-016): sesión por
  sesión, con fecha, hora de inicio/fin y páginas, en la ficha de fuente
  correspondiente — y solo cuando el investigador tenga la edición
  verificada en mano (`EDITION_VERIFIED` → `ACQUIRED` → `READING` →
  `READ`), no antes.

## Qué queda fuera de este cronograma (y por qué)

- **Sección H — contexto de formación (`SRC-201`–`SRC-209`, Kenneth
  Moreno May).** El propio manifiesto declara que "ninguna fila está
  `IDENTITY_VERIFIED`... y ninguna entra al corpus". No son lecturas de
  la tesis, son candidatos de recuperación de contexto biográfico-
  intelectual.
- **`SRC-197`–`SRC-200` (casos jurídicos: río Magpie, bosque Los Cedros,
  Mar Menor, río Marañón).** El manifiesto los marca explícitamente como
  "caso, no fuente filosófica": no se leen como bibliografía, se tratarían
  con una plantilla de caso si el investigador decide incorporarlos.
- **`SRC-PR-001`/`SRC-PR-002` (trabajo previo del propio investigador).**
  Son antecedentes archivados (`PREVIOUS_RESEARCH_BY_AUTHOR`), no corpus
  doctoral pendiente de lectura.
- **`SRC-185`.** Retirado como duplicado de `SRC-037` (ya señalado en el
  manifiesto); no es una entrada real.

Con esas exclusiones, el cronograma cubre **212 obras** de las 227
candidatas del manifiesto — incluidas las ocho de la sección J
(`SRC-219`–`SRC-226`, alcance ampliado de `PI-08`, `DEC-025`), añadidas el
2026-08-12 tras verificarse su identidad por búsqueda web.

## Fases y fundamento de cada una

El orden de fases es:

0. Herramientas metodológicas (sección F + los cuatro artículos de
   gobernanza algorítmica/reproducibilidad de la sección G).
1. Fuente del método: Derrida (sección A, `SRC-001`–`014`).
2. Genealogías nucleares en el orden exacto de `DEC-013` §1: Bodin →
   Hobbes → Schmitt → Kant → Lévinas → Heidegger → Agamben → Nancy →
   Esposito → Donaldson & Kymlicka (agrupando junto a cada autor sus
   artículos correspondientes de la sección G, por afinidad de autoría).
3. Corpus primario de apoyo restante (resto de la sección A: Aristóteles,
   Descartes, Rousseau, Bentham).
4. Bibliografía secundaria central sobre Derrida (sección B + cluster
   secundario de la sección G).
5. Estado del arte: giro político animal / comunidad interespecie (resto
   de la sección C + cluster `STATE_OF_ART` de la sección G).
6. Contexto: soberanía, comunidad, ciudadanía, biopolítica (resto de la
   sección D + cluster `CONTEXT` de la sección G).
7. Complemento y profundización (sección E + cluster `DEEPENING` de la
   sección G).
8. `PI-08` — infraestructura algorítmica, frontera humano/IA y
   transformación de la soberanía (secciones I y J completas, `DEC-023`,
   `DEC-025`): la línea más nueva y menos integrada del corpus,
   deliberadamente al final, sobre la base ya construida en las fases
   1–7. La sección J se lee inmediatamente después de la I, por ser la
   continuación del mismo eje temático dentro de la misma pregunta.

Cada fase, en el cuerpo del documento, repite su fundamento metodológico
específico antes de la tabla correspondiente.

---
"""

# entry = (src, autor, titulo_corto, prioridad, tipo)  tipo: 'L' libro, 'A' articulo, 'LL' dos obras
FASES = [
    dict(
        num=0,
        titulo="Herramientas metodológicas",
        fundamento="Historia conceptual y hermenéutica como auxiliares de la "
                    "reconstrucción genealógica y comparada (`research/methodology.md` "
                    "§1, DEC-013) — sección F del manifiesto, más los cuatro artículos "
                    "de gobernanza algorítmica/reproducibilidad de la sección G "
                    "(SRC-192–195) por afinidad temática con esta fase.",
        entries=[
            ("SRC-136", "Skinner", "\"Meaning and Understanding in the History of Ideas\"", "MEDIA", "A"),
            ("SRC-137", "Skinner", "Visions of Politics, Vol. I: Regarding Method", "MEDIA", "L"),
            ("SRC-138", "Koselleck", "Futures Past", "MEDIA", "L"),
            ("SRC-139", "Koselleck", "The Practice of Conceptual History", "MEDIA", "L"),
            ("SRC-142", "Gadamer", "Truth and Method", "MEDIA", "L"),
            ("SRC-149", "Wilkinson et al.", "\"The FAIR Guiding Principles...\"", "MEDIA", "A"),
            ("SRC-150", "Bender, Gebru, McMillan-Major, Shmitchell", "\"On the Dangers of Stochastic Parrots\"", "MEDIA", "A"),
            ("SRC-140", "Bevir", "The Logic of the History of Ideas", "BAJA", "L"),
            ("SRC-141", "Ricoeur", "Interpretation Theory", "BAJA", "L"),
            ("SRC-143", "Eco", "The Limits of Interpretation", "BAJA", "L"),
            ("SRC-144", "Moretti", "Distant Reading", "BAJA", "L"),
            ("SRC-145", "Underwood", "Distant Horizons", "BAJA", "L"),
            ("SRC-146", "Drucker", "Graphesis", "BAJA", "L"),
            ("SRC-147", "Schreibman, Siemens & Unsworth (eds.)", "A Companion to Digital Humanities", "BAJA", "L"),
            ("SRC-148", "Borgman", "Big Data, Little Data, No Data", "BAJA", "L"),
            ("SRC-192", "(autor por confirmar)", "\"Algorithmic Governmentality, Digital Sovereignty, and Agency\"", "—", "A"),
            ("SRC-193", "(autor por confirmar)", "\"Algorithmic sovereignty and democratic resilience...\"", "—", "A"),
            ("SRC-194", "(autor por confirmar)", "\"Reproducibility and explainability in digital humanities\"", "—", "A"),
            ("SRC-195", "(autor por confirmar)", "\"Reproducibility, verifiability, and computational historical research\"", "—", "A"),
        ],
    ),
    dict(
        num=1,
        titulo="Fuente del método: Derrida",
        fundamento="DEC-013 (§1): Derrida ocupa una posición distinta a la de los "
                    "demás autores del corpus — es la fuente del método (deconstrucción), "
                    "no solo un objeto sometido a él. Se lee primero como el resto de la "
                    "tesis. Sección A, SRC-001–014.",
        entries=[
            ("SRC-001", "Derrida", "Of Hospitality / De l'hospitalité", "ALTA", "L"),
            ("SRC-002", "Derrida", "Hospitality, Vol. I (ya CITED)", "ALTA", "L"),
            ("SRC-003", "Derrida", "Hospitality, Vol. II", "ALTA", "L"),
            ("SRC-004", "Derrida", "The Animal That Therefore I Am (ya CITED)", "ALTA", "L"),
            ("SRC-005", "Derrida", "The Beast and the Sovereign, Vol. I (ya CITED)", "ALTA", "L"),
            ("SRC-006", "Derrida", "The Beast and the Sovereign, Vol. II", "ALTA", "L"),
            ("SRC-007", "Derrida", "Rogues: Two Essays on Reason", "ALTA", "L"),
            ("SRC-008", "Derrida", "Politics of Friendship", "MEDIA", "L"),
            ("SRC-009", "Derrida", "Adieu to Emmanuel Levinas", "MEDIA", "L"),
            ("SRC-010", "Derrida", "Aporias", "MEDIA", "L"),
            ("SRC-012", "Derrida", "\"Force of Law\"", "MEDIA", "A"),
            ("SRC-013", "Derrida", "On Cosmopolitanism and Forgiveness", "MEDIA", "L"),
            ("SRC-011", "Derrida", "Specters of Marx", "BAJA", "L"),
            ("SRC-014", "Derrida", "The Gift of Death", "BAJA", "L"),
        ],
    ),
    dict(
        num=2,
        titulo="Genealogías nucleares (orden DEC-013 §1)",
        fundamento="Los diez autores/pares sobre los que se ejerce la lectura "
                    "deconstructiva, en el orden exacto en que DEC-013 los enumera: "
                    "Bodin, Hobbes, Schmitt, Kant, Lévinas, Heidegger, Agamben, Nancy, "
                    "Esposito, Donaldson & Kymlicka. Genealogía y análisis comparado "
                    "(auxiliares fijados en DEC-013) preparan este bloque.",
        entries=[
            ("SRC-015", "Bodin", "On Sovereignty", "ALTA", "L"),
            ("SRC-016", "Hobbes", "Leviathan", "ALTA", "L"),
            ("SRC-017", "Hobbes", "De Cive", "BAJA", "L"),
            ("SRC-018", "Hobbes", "The Elements of Law, Natural and Politic", "BAJA", "L"),
            ("SRC-019", "Schmitt", "Political Theology", "ALTA", "L"),
            ("SRC-020", "Schmitt", "The Concept of the Political", "ALTA", "L"),
            ("SRC-021", "Schmitt", "The Nomos of the Earth", "MEDIA", "L"),
            ("SRC-022", "Schmitt", "Legality and Legitimacy", "BAJA", "L"),
            ("SRC-023", "Kant", "Perpetual Peace", "ALTA", "L"),
            ("SRC-024", "Kant", "The Metaphysics of Morals", "MEDIA", "L"),
            ("SRC-025", "Levinas", "Totality and Infinity", "ALTA", "L"),
            ("SRC-026", "Levinas", "Otherwise than Being or Beyond Essence", "MEDIA", "L"),
            ("SRC-027", "Levinas", "Ethics and Infinity", "MEDIA", "L"),
            ("SRC-028", "Heidegger", "The Fundamental Concepts of Metaphysics", "ALTA", "L"),
            ("SRC-029", "Heidegger", "Being and Time", "MEDIA", "L"),
            ("SRC-030", "Agamben", "Homo Sacer", "ALTA", "L"),
            ("SRC-031", "Agamben", "The Open: Man and Animal", "ALTA", "L"),
            ("SRC-113", "Nancy", "The Inoperative Community", "ALTA", "L"),
            ("SRC-114", "Nancy", "Being Singular Plural", "MEDIA", "L"),
            ("SRC-110", "Esposito", "Communitas", "ALTA", "L"),
            ("SRC-111", "Esposito", "Immunitas", "ALTA", "L"),
            ("SRC-112", "Esposito", "Bíos: Biopolitics and Philosophy", "MEDIA", "L"),
            ("SRC-191", "Esposito", "\"Oltre la biopolitica\" / \"Beyond Biopolitics\" (2024; formato por confirmar)", "—", "A"),
            ("SRC-061", "Donaldson & Kymlicka", "Zoopolis", "ALTA", "L"),
            ("SRC-210", "Donaldson & Kymlicka", "Animals and the Right to Politics (2025)", "ALTA", "L"),
            ("SRC-062", "Donaldson & Kymlicka", "\"Animals and the Frontiers of Citizenship\"", "MEDIA", "A"),
            ("SRC-063", "Donaldson & Kymlicka", "\"A Defense of Animal Citizens and Sovereigns\"", "MEDIA", "A"),
            ("SRC-064", "Donaldson & Kymlicka", "\"Unruly Beasts...\"", "MEDIA", "A"),
            ("SRC-065", "Donaldson & Kymlicka", "\"Animals in Political Theory\"", "MEDIA", "A"),
            ("SRC-153", "Donaldson & Kymlicka", "\"Realizing Interspecies Democracy\"", "—", "A"),
            ("SRC-154", "Donaldson & Kymlicka", "\"Membership Rights for Animals\"", "—", "A"),
            ("SRC-155", "Donaldson & Kymlicka", "\"Doing Politics with Animals\"", "—", "A"),
            ("SRC-156", "Donaldson, Kymlicka & Janara", "\"Animal Ghosts at Canadian Universities\"", "—", "A"),
            ("SRC-157", "Kymlicka", "\"Rethinking Human Rights for a More-than-Human World\"", "—", "A"),
            ("SRC-196", "Kymlicka (entrevista, fuente divulgativa)", "\"...Animal Denizens and Foreigners in the Wilderness\"", "—", "A"),
        ],
    ),
    dict(
        num=3,
        titulo="Corpus primario de apoyo restante",
        fundamento="Resto de la sección A: marco antropológico auxiliar para la "
                    "frontera animalidad/comunidad, sin pertenecer al núcleo DEC-013.",
        entries=[
            ("SRC-032", "Aristotle", "Politics", "MEDIA", "L"),
            ("SRC-033", "Descartes", "Discourse on the Method (Parte V)", "MEDIA", "L"),
            ("SRC-035", "Bentham", "An Introduction to the Principles of Morals and Legislation", "MEDIA", "L"),
            ("SRC-034", "Rousseau", "Discourse on the Origin and Foundations of Inequality", "BAJA", "L"),
        ],
    ),
    dict(
        num=4,
        titulo="Bibliografía secundaria central sobre Derrida",
        fundamento="Sección B completa, más el cluster de secundaria sobre Derrida "
                    "de la sección G (SRC-184, 186, 187): interpretación crítica del "
                    "corpus primario ya leído en la Fase 1.",
        entries=[
            ("SRC-036", "Still", "Derrida and Hospitality: Theory and Practice", "ALTA", "L"),
            ("SRC-037", "Naas", "Threshold Phenomena: Derrida and the Question of Hospitality", "ALTA", "L"),
            ("SRC-046", "Lawlor", "This Is Not Sufficient", "ALTA", "L"),
            ("SRC-047", "Calarco", "Zoographies", "ALTA", "L"),
            ("SRC-038", "Naas", "Derrida From Now On", "MEDIA", "L"),
            ("SRC-040", "Beardsworth", "Derrida and the Political", "MEDIA", "L"),
            ("SRC-041", "Critchley", "The Ethics of Deconstruction", "MEDIA", "L"),
            ("SRC-048", "Calarco", "Thinking Through Animals", "MEDIA", "L"),
            ("SRC-049", "Oliver", "Animal Lessons", "MEDIA", "L"),
            ("SRC-050", "Turner", "The Animal Question in Deconstruction", "MEDIA", "L"),
            ("SRC-051", "Wolfe", "Before the Law", "MEDIA", "L"),
            ("SRC-052", "Wolfe", "Animal Rites", "MEDIA", "L"),
            ("SRC-053", "Atterton & Calarco (eds.)", "Animal Philosophy", "MEDIA", "L"),
            ("SRC-059", "Direk & Lawlor (eds.)", "A Companion to Derrida", "MEDIA", "L"),
            ("SRC-039", "Naas", "Taking on the Tradition", "BAJA", "L"),
            ("SRC-042", "Caputo", "The Prayers and Tears of Jacques Derrida", "BAJA", "L"),
            ("SRC-043", "Hägglund", "Radical Atheism", "BAJA", "L"),
            ("SRC-044", "Bennington & Derrida", "Jacques Derrida", "BAJA", "L"),
            ("SRC-045", "Lawlor", "Derrida and Husserl", "BAJA", "L"),
            ("SRC-054", "Atterton & Calarco (eds.)", "Radicalizing Levinas", "BAJA", "L"),
            ("SRC-055", "Peeters", "Derrida: A Biography", "BAJA", "L"),
            ("SRC-056", "Baring", "The Young Derrida and French Philosophy", "BAJA", "L"),
            ("SRC-057", "Howells", "Derrida: Deconstruction from Phenomenology to Ethics", "BAJA", "L"),
            ("SRC-058", "Norris", "Derrida", "BAJA", "L"),
            ("SRC-060", "Borradori", "Philosophy in a Time of Terror", "BAJA", "L"),
            ("SRC-184", "Piskorski", "Derrida and Textual Animality", "—", "L"),
            ("SRC-186", "(autor por confirmar)", "\"Jacques Derrida on the Aporias of Hospitality\"", "—", "A"),
            ("SRC-187", "(autor por confirmar)", "\"Paradise Lost in Derrida and Agamben...\"", "—", "A"),
        ],
    ),
    dict(
        num=5,
        titulo="Estado del arte: giro político animal / comunidad interespecie",
        fundamento="Resto de la sección C (SRC-066–090, sin 061–065/210 ya leídos "
                    "en la Fase 2) más el cluster STATE_OF_ART de la sección G y "
                    "SRC-175/179.",
        entries=[
            ("SRC-066", "Cochrane", "Sentientist Politics", "ALTA", "L"),
            ("SRC-074", "Meijer", "When Animals Speak", "ALTA", "L"),
            ("SRC-067", "Cochrane", "Animal Rights Without Liberation", "MEDIA", "L"),
            ("SRC-068", "Cochrane", "An Introduction to Animals and Political Theory", "MEDIA", "L"),
            ("SRC-069", "Garner", "A Theory of Justice for Animals", "MEDIA", "L"),
            ("SRC-071", "Garner & O'Sullivan (eds.)", "The Political Turn in Animal Ethics", "MEDIA", "L"),
            ("SRC-072", "O'Sullivan", "Animals, Equality and Democracy", "MEDIA", "L"),
            ("SRC-075", "Meijer", "Animal Languages", "MEDIA", "L"),
            ("SRC-076", "Nussbaum", "Frontiers of Justice", "MEDIA", "L"),
            ("SRC-077", "Nussbaum", "Justice for Animals", "MEDIA", "L"),
            ("SRC-078", "Korsgaard", "Fellow Creatures", "MEDIA", "L"),
            ("SRC-070", "Garner", "Political Animals", "BAJA", "L"),
            ("SRC-073", "Smith", "Governing Animals", "BAJA", "L"),
            ("SRC-079", "Regan", "The Case for Animal Rights", "BAJA", "L"),
            ("SRC-080", "Singer", "Animal Liberation", "BAJA", "L"),
            ("SRC-081", "Francione", "Animals, Property, and the Law", "BAJA", "L"),
            ("SRC-082", "Francione", "Introduction to Animal Rights", "BAJA", "L"),
            ("SRC-083", "Palmer", "Animal Ethics in Context", "BAJA", "L"),
            ("SRC-084", "Rowlands", "Animal Rights: Moral Theory and Practice", "BAJA", "L"),
            ("SRC-085", "Rowlands", "Can Animals Be Moral?", "BAJA", "L"),
            ("SRC-086", "Cavalieri", "The Animal Question", "BAJA", "L"),
            ("SRC-087", "Aaltola", "Animal Suffering", "BAJA", "L"),
            ("SRC-088", "Gruen", "Entangled Empathy", "BAJA", "L"),
            ("SRC-089", "Gruen", "Ethics and Animals", "BAJA", "L"),
            ("SRC-090", "Donovan & Adams (eds.)", "The Feminist Care Tradition in Animal Ethics", "BAJA", "L"),
            ("SRC-151", "Youatt", "Interspecies Politics", "—", "L"),
            ("SRC-152", "Chao et al. (eds.)", "The Promise of Multispecies Justice", "—", "L"),
            ("SRC-158", "Garner", "\"The Case for an Interspecies Theory of Democracy\"", "—", "A"),
            ("SRC-159", "Cochrane & Cojocaru", "\"Solidarity with Wild Animals\"", "—", "A"),
            ("SRC-160", "Cochrane", "\"Cosmozoopolis...\"", "—", "A"),
            ("SRC-161", "Garner", "\"Animals and Democratic Theory...\"", "—", "A"),
            ("SRC-162", "Meijer", "\"Global injustice and animals...\"", "—", "A"),
            ("SRC-163", "Meijer", "\"A Daoist-inspired Approach to Multispecies Relations\"", "—", "A"),
            ("SRC-164", "Meijer", "Multispecies Dialogues", "—", "L"),
            ("SRC-165", "Narayanan", "\"Animal-state relations...\"", "—", "A"),
            ("SRC-166", "Narayanan", "\"For multispecies liberatory futures...\"", "—", "A"),
            ("SRC-167", "Narayanan & Srinivasan", "\"...The species turn in Indian identity politics\"", "—", "A"),
            ("SRC-168", "Narayanan", "\"Mother Cow, Mother India...\"", "—", "A"),
            ("SRC-169", "Faria", "Animal Ethics in the Wild", "—", "L"),
            ("SRC-170", "Johannsen (ed.)", "Positive Duties to Wild Animals", "—", "L"),
            ("SRC-171", "Browning & Veit", "\"Positive Wild Animal Welfare\"", "—", "A"),
            ("SRC-172", "Horta & Teran", "\"Reducing Wild Animal Suffering Effectively...\"", "—", "A"),
            ("SRC-173", "(autor por confirmar)", "\"Indigenizing wild animal sovereignty\"", "—", "A"),
            ("SRC-174", "Milburn", "Food, Justice, and Animals", "—", "L"),
            ("SRC-175", "Adams, Gruen & Crary (eds.)", "The Good It Promises, the Harm It Does", "—", "L"),
            ("SRC-179", "Bernet Kempers", "\"What Are Animal Rights For?\"", "—", "A"),
        ],
    ),
    dict(
        num=6,
        titulo="Contexto: soberanía, comunidad, ciudadanía, biopolítica",
        fundamento="Resto de la sección D (sin Nancy/Esposito, ya leídos en la "
                    "Fase 2) más el cluster CONTEXT de la sección G.",
        entries=[
            ("SRC-091", "Bartelson", "A Genealogy of Sovereignty", "MEDIA", "L"),
            ("SRC-096", "Brown", "Walled States, Waning Sovereignty", "MEDIA", "L"),
            ("SRC-099", "Arendt", "The Origins of Totalitarianism", "MEDIA", "L"),
            ("SRC-100", "Arendt", "The Human Condition", "MEDIA", "L"),
            ("SRC-102", "Foucault", "Society Must Be Defended", "MEDIA", "L"),
            ("SRC-103", "Foucault", "Security, Territory, Population", "MEDIA", "L"),
            ("SRC-104", "Foucault", "The Birth of Biopolitics", "MEDIA", "L"),
            ("SRC-106", "Mbembe", "Necropolitics", "MEDIA", "L"),
            ("SRC-107", "Butler", "Precarious Life", "MEDIA", "L"),
            ("SRC-108", "Butler", "Frames of War", "MEDIA", "L"),
            ("SRC-092", "Hinsley", "Sovereignty", "BAJA", "L"),
            ("SRC-093", "Krasner", "Sovereignty: Organized Hypocrisy", "BAJA", "L"),
            ("SRC-094", "Walker", "Inside/Outside", "BAJA", "L"),
            ("SRC-095", "Agnew", "\"Sovereignty Regimes...\"", "BAJA", "A"),
            ("SRC-097", "Balibar", "We, the People of Europe?", "BAJA", "L"),
            ("SRC-098", "Balibar", "Citizenship", "BAJA", "L"),
            ("SRC-101", "Arendt", "On Revolution", "BAJA", "L"),
            ("SRC-105", "Foucault", "The History of Sexuality, Vol. 1", "BAJA", "L"),
            ("SRC-109", "Rancière", "Disagreement", "BAJA", "L"),
            ("SRC-115", "Hardt & Negri", "Empire", "BAJA", "L"),
            ("SRC-176", "Fasel & Butler", "Animal Rights Law", "—", "L"),
            ("SRC-177", "Adenitire & Fasel", "Animals and the Constitution", "—", "L"),
            ("SRC-178", "Deckha", "Animals as Legal Beings", "—", "L"),
            ("SRC-183", "Cimatti & Salzani (eds.)", "The Biopolitical Animal", "—", "L"),
            ("SRC-188", "Di Cesare", "Resident Foreigners", "—", "L"),
            ("SRC-189", "Lejeune, Pagès-El Karoui, Schmoll & Thiollet (eds.)", "Migration, Urbanity and Cosmopolitanism in a Globalized World", "—", "L"),
            ("SRC-190", "Piasentier & Raimondi (eds.)", "Debating Biopolitics", "—", "L"),
        ],
    ),
    dict(
        num=7,
        titulo="Complemento y profundización",
        fundamento="Sección E completa (posthumanismo, estudios multiespecie, "
                    "etología) más el cluster DEEPENING de la sección G.",
        entries=[
            ("SRC-116", "Haraway", "The Companion Species Manifesto", "MEDIA", "L"),
            ("SRC-117", "Haraway", "When Species Meet", "MEDIA", "L"),
            ("SRC-118", "Haraway", "Staying with the Trouble", "MEDIA", "L"),
            ("SRC-119", "Wolfe", "What Is Posthumanism?", "MEDIA", "L"),
            ("SRC-121", "Braidotti", "The Posthuman", "MEDIA", "L"),
            ("SRC-124", "Latour", "Politics of Nature", "MEDIA", "L"),
            ("SRC-132", "Despret", "What Would Animals Say If We Asked the Right Questions?", "MEDIA", "L"),
            ("SRC-134", "von Uexküll", "A Foray into the Worlds of Animals and Humans", "MEDIA", "L"),
            ("SRC-120", "Hayles", "How We Became Posthuman", "BAJA", "L"),
            ("SRC-122", "Braidotti", "Posthuman Knowledge", "BAJA", "L"),
            ("SRC-123", "Latour", "We Have Never Been Modern", "BAJA", "L"),
            ("SRC-125", "Latour", "Facing Gaia", "BAJA", "L"),
            ("SRC-126", "Descola", "Beyond Nature and Culture", "BAJA", "L"),
            ("SRC-127", "Viveiros de Castro", "Cannibal Metaphysics", "BAJA", "L"),
            ("SRC-128", "Kohn", "How Forests Think", "BAJA", "L"),
            ("SRC-129", "Tsing", "The Mushroom at the End of the World", "BAJA", "L"),
            ("SRC-130", "van Dooren", "Flight Ways", "BAJA", "L"),
            ("SRC-131", "Rose", "Wild Dog Dreaming", "BAJA", "L"),
            ("SRC-133", "Despret", "Living as a Bird", "BAJA", "L"),
            ("SRC-135", "de Waal", "Are We Smart Enough to Know How Smart Animals Are?", "BAJA", "L"),
            ("SRC-180", "Braidotti", "Posthuman Feminism", "—", "L"),
            ("SRC-181", "Ferrando", "The Art of Being Posthuman", "—", "L"),
            ("SRC-182", "Calarco", "The Three Ethologies", "—", "L"),
        ],
    ),
    dict(
        num=8,
        titulo="PI-08: infraestructura algorítmica, frontera humano/IA y transformación de la soberanía",
        fundamento="Secciones I (SRC-211–218, DEC-023) y J (SRC-219–226, "
                    "DEC-025) completas. Línea más nueva y menos integrada del "
                    "corpus: se lee al final, sobre la base ya construida en las "
                    "fases 1–7, tal como la extiende explícitamente hacia \"un "
                    "objeto contemporáneo concreto\" sin sustituir el campo "
                    "crítico privilegiado (el animal). La sección J (frontera "
                    "humano/IA, autonomía algorítmica, control bélico y "
                    "biopolítico) se lee justo después de la I, como ampliación "
                    "del mismo eje, no como línea aparte.",
        entries=[
            ("SRC-211", "Varoufakis", "Technofeudalism: What Killed Capitalism", "—", "L"),
            ("SRC-212", "Durand", "How Silicon Valley Unleashed Techno-Feudalism", "—", "L"),
            ("SRC-213", "Zuboff", "The Age of Surveillance Capitalism", "—", "L"),
            ("SRC-214", "Srnicek", "Platform Capitalism", "—", "L"),
            ("SRC-215", "Rouvroy & Berns", "\"Gouvernementalité algorithmique et perspectives d'émancipation\"", "—", "A"),
            ("SRC-216", "Stiegler", "The Age of Disruption", "—", "L"),
            ("SRC-217", "Mbembe", "Brutalisme", "—", "L"),
            ("SRC-218", "Byung-Chul Han", "Psychopolitics + Infocracy (dos obras, una fila)", "—", "LL"),
            ("SRC-219", "Bostrom", "Superintelligence: Paths, Dangers, Strategies", "—", "L"),
            ("SRC-220", "Crawford", "Atlas of AI", "—", "L"),
            ("SRC-221", "Pasquale", "The Black Box Society", "—", "L"),
            ("SRC-222", "Pasquale", "New Laws of Robotics", "—", "L"),
            ("SRC-223", "Singer, P. W.", "Wired for War", "—", "L"),
            ("SRC-224", "Kello", "The Virtual Weapon and International Order", "—", "L"),
            ("SRC-225", "Hui", "Recursivity and Contingency", "—", "L"),
            ("SRC-226", "Floridi", "The Fourth Revolution", "—", "L"),
        ],
    ),
]


def peso(fase_num, prioridad, tipo):
    """Semanas que ocupa una entrada. Regla ajustable: ver nota de ritmo en HEADER."""
    if tipo == "A":
        return 0.5
    if tipo == "LL":
        return 2.0
    if fase_num <= 2 and prioridad == "ALTA":
        return 2.0
    return 1.0


def fmt_date(d):
    meses = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    return f"{d.day} {meses[d.month]} {d.year}"


def main():
    cum_weeks = 0.0
    total_entries = 0
    lines = [HEADER]
    for fase in FASES:
        lines.append(f"\n## Fase {fase['num']} — {fase['titulo']}\n")
        lines.append(fase["fundamento"] + "\n")
        lines.append("| SRC | Autor(es) | Obra | Prioridad | Inicio | Fin |")
        lines.append("|---|---|---|---|---|---|")
        for src, autor, titulo, prioridad, tipo in fase["entries"]:
            w = peso(fase["num"], prioridad, tipo)
            start = START + datetime.timedelta(weeks=cum_weeks)
            end = START + datetime.timedelta(weeks=cum_weeks + w) - datetime.timedelta(days=1)
            lines.append(f"| {src} | {autor} | {titulo} | {prioridad} | {fmt_date(start)} | {fmt_date(end)} |")
            cum_weeks += w
            total_entries += 1

    end_total = START + datetime.timedelta(weeks=cum_weeks) - datetime.timedelta(days=1)
    lines.append("")
    lines.append(
        f"**Fin del cronograma (a este ritmo estimado): {fmt_date(end_total)} "
        f"(~{cum_weeks:g} semanas, ~{cum_weeks / 52.1785:.1f} años).**"
    )

    with open(OUTPUT_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Escrito {OUTPUT_PATH}: {total_entries} obras, {cum_weeks:g} semanas, "
          f"fin {fmt_date(end_total)}")


if __name__ == "__main__":
    main()

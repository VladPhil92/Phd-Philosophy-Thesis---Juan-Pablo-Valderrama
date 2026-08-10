# Library manifest / registro canónico de fuentes

**Estado de lectura:** `CANDIDATE` en bloque — ningún registro de este documento ha sido
promovido a `bibliography.bib`.

## Qué es este documento y qué NO es

Este documento es el **manifest canónico de fuentes y candidatos** para la selección progresiva del
corpus. Registra qué obras podrían ser pertinentes y por qué, con su nivel de
verificación declarado honestamente. **No es** el catálogo bibliográfico
canónico (eso es [`bibliography.bib`](bibliography.bib)), no acredita lectura
de ninguna obra, y ninguna entrada aquí puede citarse en una ficha de
argumento (`ARG-*`) hasta ser promovida a `bibliography.bib` con edición
verificada.

Esta distinción es la misma que exige `.claude/rules/sources.md`: «no crees
fichas de fuentes especulativas para obras que el investigador aún no ha
incorporado realmente al corpus». Un candidato en este manifest no es una fuente
incorporada.

### Origen de las entradas y su nivel real de verificación

- **SRC-001 a SRC-150** proceden de una propuesta del investigador, quien
  declara haberla contrastado con catálogos editoriales y bibliografías
  especializadas (p. ej. Stanford Encyclopedia of Philosophy, University of
  Chicago Press, Cambridge University Press, Oxford). **Esta sesión no ha
  verificado de forma independiente cada una de esas 150 entradas** — se
  registran con el estado `CANDIDATE` y la nota `identidad declarada por el
  investigador, no verificada de forma independiente en esta sesión`.
- **SRC-151 a SRC-200** fueron localizadas mediante búsqueda web directa en
  esta sesión (2020–2026, ampliación solicitada). Cada una incluye la URL
  usada para confirmar su existencia. Se marcan `IDENTITY_VERIFIED`: se
  confirmó que la obra/artículo existe con ese autor, título y año
  aproximado, **no** que su edición, DOI/ISBN exactos o contenido hayan sido
  verificados, y mucho menos que hayan sido leídos.
- Ninguna entrada de este documento se marca `EDITION_VERIFIED`,
  `ACQUIRED`, `READING`, `READ` ni `CITED`. Esos estados solo los asigna el
  investigador cuando adquiere y verifica la edición real que va a citar.

## Convención de estados

```text
CANDIDATE
    ↓
IDENTITY_VERIFIED       (se confirmó que la obra existe con esos metadatos aproximados)
    ↓
EDITION_VERIFIED         (el investigador confirmó edición, traductor, ISBN/DOI exactos)
    ↓
ACQUIRED                 (el investigador tiene acceso legítimo a esa edición)
    ↓
READING
    ↓
READ
    ↓
CITED                    (solo entonces puede entrar a bibliography.bib y a un ARG-*)
```

Ningún script ni agente de IA puede promover una entrada más allá de
`IDENTITY_VERIFIED` de forma autónoma. `EDITION_VERIFIED` en adelante requiere
al investigador con el objeto físico o la edición digital autorizada en mano.

## Clasificación funcional

| Etiqueta | Significado | Categorías de origen |
|---|---|---|
| `PRIMARY_CORE` | Interviene directamente en la construcción de la tesis, lectura obligatoria | A (prioridad máxima) |
| `PRIMARY_SUPPORTING` | Corpus primario de apoyo | A (resto) |
| `SECONDARY_CORE` | Interpretación crítica del corpus primario | B |
| `STATE_OF_ART` | Estado del arte del giro político animal / comunidad interespecie | C, más una parte de G |
| `CONTEXT` | Soberanía, comunidad, frontera, ciudadanía, biopolítica | D, más una parte de G |
| `DEEPENING` / `COMPLEMENTARY` | Posthumanismo, estudios multiespecie, antropología, etología (se trata como un solo nivel; no se distinguen ambas etiquetas mientras el corpus no lo requiera) | E, más una parte de G |
| `METHODOLOGY` | Método filosófico, historia conceptual, trazabilidad computacional | F, más una parte de G |

## Relación con `research/methodology.md`

La selección final de corpus sigue marcada `DECISIÓN HUMANA REQUERIDA` en
`research/methodology.md` §2. Este manifest es una propuesta de partida para esa
decisión, no su resolución. Ningún criterio de selección se considera
adoptado hasta que el investigador lo registre allí.

## Lectura de primera ronda (propuesta del investigador, pendiente de confirmación)

`PRIORIDAD: ALTA` marca las ~25–30 obras que el investigador propuso como
lectura doctoral obligatoria de la primera ronda. Es una propuesta, no una
decisión cerrada.

---

## A. Fuentes principales — corpus primario (SRC-001–SRC-035)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-001 | Derrida, J. | Of Hospitality / De l'hospitalité | 1997/2000 | PRIMARY_CORE | ALTA | PI-01, PI-05 | CANDIDATE |
| SRC-002 | Derrida, J. | Hospitality, Volume I (University of Chicago Press) | 2023 | PRIMARY_CORE | ALTA | PI-01, PI-05 | CANDIDATE |
| SRC-003 | Derrida, J. | Hospitality, Volume II (University of Chicago Press) | 2024 | PRIMARY_CORE | ALTA | PI-01, PI-05 | CANDIDATE |
| SRC-004 | Derrida, J. | The Animal That Therefore I Am | 2006/2008 | PRIMARY_CORE | ALTA | PI-04 | CANDIDATE |
| SRC-005 | Derrida, J. | The Beast and the Sovereign, Vol. I | 2009 | PRIMARY_CORE | ALTA | PI-02, PI-04 | CANDIDATE |
| SRC-006 | Derrida, J. | The Beast and the Sovereign, Vol. II | 2011/2017 | PRIMARY_CORE | ALTA | PI-02, PI-04 | CANDIDATE |
| SRC-007 | Derrida, J. | Rogues: Two Essays on Reason | 2003/2005 | PRIMARY_CORE | ALTA | PI-02, PI-07 | CANDIDATE |
| SRC-008 | Derrida, J. | Politics of Friendship | 1994/1997 | PRIMARY_SUPPORTING | MEDIA | PI-06 | CANDIDATE |
| SRC-009 | Derrida, J. | Adieu to Emmanuel Levinas | 1997/1999 | PRIMARY_SUPPORTING | MEDIA | PI-05, PI-07 | CANDIDATE |
| SRC-010 | Derrida, J. | Aporias | 1996 | PRIMARY_SUPPORTING | MEDIA | PI-01 | CANDIDATE |
| SRC-011 | Derrida, J. | Specters of Marx | 1993/1994 | PRIMARY_SUPPORTING | BAJA | PI-07 | CANDIDATE |
| SRC-012 | Derrida, J. | "Force of Law: The 'Mystical Foundation of Authority'" | 1990 | PRIMARY_SUPPORTING | MEDIA | PI-02 | CANDIDATE |
| SRC-013 | Derrida, J. | On Cosmopolitanism and Forgiveness | 2001 | PRIMARY_SUPPORTING | MEDIA | PI-05 | CANDIDATE |
| SRC-014 | Derrida, J. | The Gift of Death | 1992/1995 | PRIMARY_SUPPORTING | BAJA | PI-07 | CANDIDATE |
| SRC-015 | Bodin, J. | On Sovereignty: Four Chapters from The Six Books of the Commonwealth | 1576/1992 | PRIMARY_CORE | ALTA | PI-02 | CANDIDATE |
| SRC-016 | Hobbes, T. | Leviathan | 1651 | PRIMARY_CORE | ALTA | PI-02 | CANDIDATE |
| SRC-017 | Hobbes, T. | De Cive | 1642 | PRIMARY_SUPPORTING | BAJA | PI-02 | CANDIDATE |
| SRC-018 | Hobbes, T. | The Elements of Law, Natural and Politic | 1640/1650 | PRIMARY_SUPPORTING | BAJA | PI-02 | CANDIDATE |
| SRC-019 | Schmitt, C. | Political Theology | 1922 | PRIMARY_CORE | ALTA | PI-02 | CANDIDATE |
| SRC-020 | Schmitt, C. | The Concept of the Political | 1932 | PRIMARY_CORE | ALTA | PI-02 | CANDIDATE |
| SRC-021 | Schmitt, C. | The Nomos of the Earth | 1950 | PRIMARY_SUPPORTING | MEDIA | PI-02 | CANDIDATE |
| SRC-022 | Schmitt, C. | Legality and Legitimacy | 1932 | PRIMARY_SUPPORTING | BAJA | PI-02 | CANDIDATE |
| SRC-023 | Kant, I. | Perpetual Peace: A Philosophical Sketch | 1795 | PRIMARY_CORE | ALTA | PI-05 | CANDIDATE |
| SRC-024 | Kant, I. | The Metaphysics of Morals | 1797 | PRIMARY_SUPPORTING | MEDIA | PI-02, PI-05 | CANDIDATE |
| SRC-025 | Levinas, E. | Totality and Infinity | 1961 | PRIMARY_CORE | ALTA | PI-05, PI-07 | CANDIDATE |
| SRC-026 | Levinas, E. | Otherwise than Being or Beyond Essence | 1974 | PRIMARY_SUPPORTING | MEDIA | PI-07 | CANDIDATE |
| SRC-027 | Levinas, E. | Ethics and Infinity | 1982/1985 | PRIMARY_SUPPORTING | MEDIA | PI-07 | CANDIDATE |
| SRC-028 | Heidegger, M. | The Fundamental Concepts of Metaphysics: World, Finitude, Solitude | 1929–30/1983 | PRIMARY_CORE | ALTA | PI-03, PI-04 | CANDIDATE |
| SRC-029 | Heidegger, M. | Being and Time | 1927 | PRIMARY_SUPPORTING | MEDIA | PI-03 | CANDIDATE |
| SRC-030 | Agamben, G. | Homo Sacer: Sovereign Power and Bare Life | 1995/1998 | PRIMARY_CORE | ALTA | PI-02 | CANDIDATE |
| SRC-031 | Agamben, G. | The Open: Man and Animal | 2002/2004 | PRIMARY_CORE | ALTA | PI-04 | CANDIDATE |
| SRC-032 | Aristotle | Politics | — | PRIMARY_SUPPORTING | MEDIA | PI-03 | CANDIDATE |
| SRC-033 | Descartes, R. | Discourse on the Method (esp. Parte V) | 1637 | PRIMARY_SUPPORTING | MEDIA | PI-03, PI-04 | CANDIDATE |
| SRC-034 | Rousseau, J.-J. | Discourse on the Origin and Foundations of Inequality Among Men | 1755 | PRIMARY_SUPPORTING | BAJA | PI-03 | CANDIDATE |
| SRC-035 | Bentham, J. | An Introduction to the Principles of Morals and Legislation | 1789 | PRIMARY_SUPPORTING | MEDIA | PI-04 | CANDIDATE |

## B. Bibliografía secundaria central (SRC-036–SRC-060)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-036 | Still, J. | Derrida and Hospitality: Theory and Practice | 2010 | SECONDARY_CORE | ALTA | PI-01, PI-05 | CANDIDATE |
| SRC-037 | Naas, M. | Threshold Phenomena: Derrida and the Question of Hospitality | 2024 | SECONDARY_CORE | ALTA | PI-01, PI-05 | CANDIDATE |
| SRC-038 | Naas, M. | Derrida From Now On | 2008 | SECONDARY_CORE | MEDIA | PI-01 | CANDIDATE |
| SRC-039 | Naas, M. | Taking on the Tradition: Jacques Derrida and the Legacies of Deconstruction | 2002 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-040 | Beardsworth, R. | Derrida and the Political | 1996 | SECONDARY_CORE | MEDIA | PI-02 | CANDIDATE |
| SRC-041 | Critchley, S. | The Ethics of Deconstruction: Derrida and Levinas | 1992 | SECONDARY_CORE | MEDIA | PI-07 | CANDIDATE |
| SRC-042 | Caputo, J. D. | The Prayers and Tears of Jacques Derrida: Religion without Religion | 1997 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-043 | Hägglund, M. | Radical Atheism: Derrida and the Time of Life | 2008 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-044 | Bennington, G. & Derrida, J. | Jacques Derrida | 1991/1993 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-045 | Lawlor, L. | Derrida and Husserl: The Basic Problem of Phenomenology | 2002 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-046 | Lawlor, L. | This Is Not Sufficient: An Essay on Animality and Human Nature in Derrida | 2007 | SECONDARY_CORE | ALTA | PI-04 | CANDIDATE |
| SRC-047 | Calarco, M. | Zoographies: The Question of the Animal from Heidegger to Derrida | 2008 | SECONDARY_CORE | ALTA | PI-04 | CANDIDATE |
| SRC-048 | Calarco, M. | Thinking Through Animals: Identity, Difference, Indistinction | 2015 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-049 | Oliver, K. | Animal Lessons: How They Teach Us to Be Human | 2009 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-050 | Turner, L. | The Animal Question in Deconstruction | 2013 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-051 | Wolfe, C. | Before the Law: Humans and Other Animals in a Biopolitical Frame | 2013 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-052 | Wolfe, C. | Animal Rites: American Culture, the Discourse of Species, and Posthumanist Theory | 2003 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-053 | Atterton, P. & Calarco, M. (eds.) | Animal Philosophy: Essential Readings in Continental Thought | 2004 | SECONDARY_CORE | MEDIA | PI-04 | CANDIDATE |
| SRC-054 | Atterton, P. & Calarco, M. (eds.) | Radicalizing Levinas | 2010 | SECONDARY_CORE | BAJA | PI-07 | CANDIDATE |
| SRC-055 | Peeters, B. | Derrida: A Biography | 2010/2013 | SECONDARY_CORE | BAJA | — | CANDIDATE |
| SRC-056 | Baring, E. | The Young Derrida and French Philosophy, 1945–1968 | 2011 | SECONDARY_CORE | BAJA | — | CANDIDATE |
| SRC-057 | Howells, C. | Derrida: Deconstruction from Phenomenology to Ethics | 1998 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-058 | Norris, C. | Derrida | 1987 | SECONDARY_CORE | BAJA | PI-01 | CANDIDATE |
| SRC-059 | Direk, Z. & Lawlor, L. (eds.) | A Companion to Derrida | 2014 | SECONDARY_CORE | MEDIA | PI-01 | CANDIDATE |
| SRC-060 | Borradori, G. | Philosophy in a Time of Terror: Dialogues with Habermas and Derrida | 2003 | SECONDARY_CORE | BAJA | PI-02 | CANDIDATE |

## C. Comunidad política interespecie y "political turn" (SRC-061–SRC-090)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-061 | Donaldson, S. & Kymlicka, W. | Zoopolis: A Political Theory of Animal Rights | 2011 | STATE_OF_ART | ALTA | PI-02, PI-04, PI-06 | CANDIDATE |
| SRC-062 | Donaldson, S. & Kymlicka, W. | "Animals and the Frontiers of Citizenship" | 2014 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-063 | Donaldson, S. & Kymlicka, W. | "A Defense of Animal Citizens and Sovereigns" | 2013 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-064 | Donaldson, S. & Kymlicka, W. | "Unruly Beasts: Animal Citizens and the Threat of Tyranny" | 2014 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-065 | Donaldson, S. & Kymlicka, W. | "Animals in Political Theory" (Oxford Handbook of Animal Studies) | — | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-066 | Cochrane, A. | Sentientist Politics: A Theory of Global Inter-Species Justice | 2018 | STATE_OF_ART | ALTA | PI-02, PI-06 | CANDIDATE |
| SRC-067 | Cochrane, A. | Animal Rights Without Liberation | 2012 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-068 | Cochrane, A. | An Introduction to Animals and Political Theory | 2010 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-069 | Garner, R. | A Theory of Justice for Animals: Animal Rights in a Nonideal World | 2013 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-070 | Garner, R. | Political Animals: Animal Protection Politics in Britain and the United States | 1998 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-071 | Garner, R. & O'Sullivan, S. (eds.) | The Political Turn in Animal Ethics | 2016 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-072 | O'Sullivan, S. | Animals, Equality and Democracy | 2011 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-073 | Smith, K. K. | Governing Animals: Animal Welfare and the Liberal State | 2012 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-074 | Meijer, E. | When Animals Speak: Toward an Interspecies Democracy | 2019 | STATE_OF_ART | ALTA | PI-04, PI-06 | CANDIDATE |
| SRC-075 | Meijer, E. | Animal Languages: The Secret Conversations of the Living World | 2019 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-076 | Nussbaum, M. C. | Frontiers of Justice: Disability, Nationality, Species Membership | 2006 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-077 | Nussbaum, M. C. | Justice for Animals: Our Collective Responsibility | 2022 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-078 | Korsgaard, C. M. | Fellow Creatures: Our Obligations to the Other Animals | 2018 | STATE_OF_ART | MEDIA | PI-06 | CANDIDATE |
| SRC-079 | Regan, T. | The Case for Animal Rights | 1983 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-080 | Singer, P. | Animal Liberation | 1975 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-081 | Francione, G. L. | Animals, Property, and the Law | 1995 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-082 | Francione, G. L. | Introduction to Animal Rights: Your Child or the Dog? | 2000 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-083 | Palmer, C. | Animal Ethics in Context | 2010 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-084 | Rowlands, M. | Animal Rights: Moral Theory and Practice | 1998/2009 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-085 | Rowlands, M. | Can Animals Be Moral? | 2012 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-086 | Cavalieri, P. | The Animal Question: Why Nonhuman Animals Deserve Human Rights | 2001 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-087 | Aaltola, E. | Animal Suffering: Philosophy and Culture | 2012 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-088 | Gruen, L. | Entangled Empathy: An Alternative Ethic for Our Relationships with Animals | 2015 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-089 | Gruen, L. | Ethics and Animals: An Introduction | 2011 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-090 | Donovan, J. & Adams, C. J. (eds.) | The Feminist Care Tradition in Animal Ethics | 2007 | STATE_OF_ART | BAJA | PI-06 | CANDIDATE |
| SRC-201 | Donaldson, S. & Kymlicka, W. | Animals and the Right to Politics | 2025 | STATE_OF_ART | ALTA | PI-02, PI-04, PI-06 | CANDIDATE |

### Auditoría focal del giro político (2026-08-10)

La auditoría identificó los catálogos editoriales oficiales contra los cuales
deben cotejarse autoría, título, año y editorial. El entorno bloqueó el acceso
automatizado a esos catálogos; por ello no se declara una confirmación que no
pudo completarse y los seis registros permanecen `CANDIDATE`. Tampoco se
confirmaron la edición que usará el investigador, ISBN/DOI, adquisición, lectura
o interpretación.

| Obra | Editorial por cotejar | Fuente oficial identificada | Observación |
|---|---|---|---|
| *Zoopolis* | Oxford University Press | [Oxford Academic](https://academic.oup.com/search-results?q=Zoopolis%3A%20A%20Political%20Theory%20of%20Animal%20Rights) | Estatutos diferenciados por verificar mediante lectura directa. |
| *Sentientist Politics* | Oxford University Press | [Oxford Academic](https://academic.oup.com/search-results?q=Sentientist%20Politics) | Capítulos sobre democracia y soberanía pendientes de lectura directa. |
| *A Theory of Justice for Animals* | Oxford University Press | [Oxford Academic](https://academic.oup.com/search-results?q=A%20Theory%20of%20Justice%20for%20Animals) | Relación con teoría no ideal pendiente de lectura directa. |
| *Animals, Equality and Democracy* | Palgrave Macmillan | [Springer Nature](https://link.springer.com/book/10.1057/9780230349186) | Análisis institucional pendiente de lectura directa. |
| *When Animals Speak* | New York University Press | [NYU Press](https://nyupress.org/9781479863136/when-animals-speak/) | Agencia y democracia interespecie pendientes de lectura directa. |
| *Animals and the Right to Politics* | Oxford University Press | [Oxford Academic](https://academic.oup.com/search-results?q=Animals%20and%20the%20Right%20to%20Politics) | Desarrollo contemporáneo pendiente de lectura directa. |

El capítulo panorámico «Animals in Political Theory» ya estaba registrado y se conserva como
`CANDIDATE`: puede orientar el estado del arte, pero no sustituye las monografías
ni se promueve sin verificación adicional.

## D. Contexto: soberanía, frontera, comunidad, ciudadanía, biopolítica (SRC-091–SRC-115)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-091 | Bartelson, J. | A Genealogy of Sovereignty | 1995 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-092 | Hinsley, F. H. | Sovereignty | 1986 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-093 | Krasner, S. D. | Sovereignty: Organized Hypocrisy | 1999 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-094 | Walker, R. B. J. | Inside/Outside: International Relations as Political Theory | 1993 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-095 | Agnew, J. | "Sovereignty Regimes: Territoriality and State Authority in Contemporary World Politics" | 2005 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-096 | Brown, W. | Walled States, Waning Sovereignty | 2010 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-097 | Balibar, É. | We, the People of Europe? Reflections on Transnational Citizenship | 2004 | CONTEXT | BAJA | PI-06 | CANDIDATE |
| SRC-098 | Balibar, É. | Citizenship | 2015 | CONTEXT | BAJA | PI-06 | CANDIDATE |
| SRC-099 | Arendt, H. | The Origins of Totalitarianism | 1951 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-100 | Arendt, H. | The Human Condition | 1958 | CONTEXT | MEDIA | PI-03 | CANDIDATE |
| SRC-101 | Arendt, H. | On Revolution | 1963 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-102 | Foucault, M. | Society Must Be Defended | 1975–76/1997 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-103 | Foucault, M. | Security, Territory, Population | 1977–78/2004 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-104 | Foucault, M. | The Birth of Biopolitics | 1978–79/2004 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-105 | Foucault, M. | The History of Sexuality, Vol. 1 | 1976 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-106 | Mbembe, A. | Necropolitics | 2019 | CONTEXT | MEDIA | PI-02 | CANDIDATE |
| SRC-107 | Butler, J. | Precarious Life: The Powers of Mourning and Violence | 2004 | CONTEXT | MEDIA | PI-07 | CANDIDATE |
| SRC-108 | Butler, J. | Frames of War: When Is Life Grievable? | 2009 | CONTEXT | MEDIA | PI-07 | CANDIDATE |
| SRC-109 | Rancière, J. | Disagreement: Politics and Philosophy | 1995/1999 | CONTEXT | BAJA | PI-02 | CANDIDATE |
| SRC-110 | Esposito, R. | Communitas: The Origin and Destiny of Community | 1998/2010 | CONTEXT | ALTA | PI-07 | CANDIDATE |
| SRC-111 | Esposito, R. | Immunitas: The Protection and Negation of Life | 2002/2011 | CONTEXT | ALTA | PI-07 | CANDIDATE |
| SRC-112 | Esposito, R. | Bíos: Biopolitics and Philosophy | 2004/2008 | CONTEXT | MEDIA | PI-02, PI-07 | CANDIDATE |
| SRC-113 | Nancy, J.-L. | The Inoperative Community | 1986/1991 | CONTEXT | ALTA | PI-07 | CANDIDATE |
| SRC-114 | Nancy, J.-L. | Being Singular Plural | 1996/2000 | CONTEXT | MEDIA | PI-07 | CANDIDATE |
| SRC-115 | Hardt, M. & Negri, A. | Empire | 2000 | CONTEXT | BAJA | PI-02 | CANDIDATE |

## E. Complemento y profundización (SRC-116–SRC-135)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-116 | Haraway, D. J. | The Companion Species Manifesto | 2003 | DEEPENING | MEDIA | PI-04, PI-06 | CANDIDATE |
| SRC-117 | Haraway, D. J. | When Species Meet | 2008 | DEEPENING | MEDIA | PI-04, PI-06 | CANDIDATE |
| SRC-118 | Haraway, D. J. | Staying with the Trouble: Making Kin in the Chthulucene | 2016 | DEEPENING | MEDIA | PI-06 | CANDIDATE |
| SRC-119 | Wolfe, C. | What Is Posthumanism? | 2010 | DEEPENING | MEDIA | PI-04 | CANDIDATE |
| SRC-120 | Hayles, N. K. | How We Became Posthuman | 1999 | DEEPENING | BAJA | PI-04 | CANDIDATE |
| SRC-121 | Braidotti, R. | The Posthuman | 2013 | DEEPENING | MEDIA | PI-04 | CANDIDATE |
| SRC-122 | Braidotti, R. | Posthuman Knowledge | 2019 | DEEPENING | BAJA | PI-04 | CANDIDATE |
| SRC-123 | Latour, B. | We Have Never Been Modern | 1991/1993 | DEEPENING | BAJA | PI-03 | CANDIDATE |
| SRC-124 | Latour, B. | Politics of Nature: How to Bring the Sciences into Democracy | 1999/2004 | DEEPENING | MEDIA | PI-06 | CANDIDATE |
| SRC-125 | Latour, B. | Facing Gaia: Eight Lectures on the New Climatic Regime | 2015/2017 | DEEPENING | BAJA | — | CANDIDATE |
| SRC-126 | Descola, P. | Beyond Nature and Culture | 2005/2013 | DEEPENING | BAJA | PI-03 | CANDIDATE |
| SRC-127 | Viveiros de Castro, E. | Cannibal Metaphysics | 2009/2014 | DEEPENING | BAJA | PI-03 | CANDIDATE |
| SRC-128 | Kohn, E. | How Forests Think: Toward an Anthropology Beyond the Human | 2013 | DEEPENING | BAJA | PI-03 | CANDIDATE |
| SRC-129 | Tsing, A. L. | The Mushroom at the End of the World | 2015 | DEEPENING | BAJA | — | CANDIDATE |
| SRC-130 | van Dooren, T. | Flight Ways: Life and Loss at the Edge of Extinction | 2014 | DEEPENING | BAJA | — | CANDIDATE |
| SRC-131 | Rose, D. B. | Wild Dog Dreaming: Love and Extinction | 2011 | DEEPENING | BAJA | — | CANDIDATE |
| SRC-132 | Despret, V. | What Would Animals Say If We Asked the Right Questions? | 2016 | DEEPENING | MEDIA | PI-04 | CANDIDATE |
| SRC-133 | Despret, V. | Living as a Bird | 2019/2021 | DEEPENING | BAJA | PI-04 | CANDIDATE |
| SRC-134 | von Uexküll, J. | A Foray into the Worlds of Animals and Humans | 1934/2010 | DEEPENING | MEDIA | PI-04 | CANDIDATE |
| SRC-135 | de Waal, F. | Are We Smart Enough to Know How Smart Animals Are? | 2016 | DEEPENING | BAJA | PI-04 | CANDIDATE |

## F. Metodología, historia conceptual y repositorio digital (SRC-136–SRC-150)

| SRC | Autor(es) | Título | Año | Clasificación | Prioridad | PI relacionadas | Estado |
|---|---|---|---|---|---|---|---|
| SRC-136 | Skinner, Q. | "Meaning and Understanding in the History of Ideas" | 1969 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-137 | Skinner, Q. | Visions of Politics, Vol. I: Regarding Method | 2002 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-138 | Koselleck, R. | Futures Past: On the Semantics of Historical Time | 1979/2004 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-139 | Koselleck, R. | The Practice of Conceptual History | 2002 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-140 | Bevir, M. | The Logic of the History of Ideas | 1999 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-141 | Ricoeur, P. | Interpretation Theory: Discourse and the Surplus of Meaning | 1976 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-142 | Gadamer, H.-G. | Truth and Method | 1960 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-143 | Eco, U. | The Limits of Interpretation | 1990 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-144 | Moretti, F. | Distant Reading | 2013 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-145 | Underwood, T. | Distant Horizons: Digital Evidence and Literary Change | 2019 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-146 | Drucker, J. | Graphesis: Visual Forms of Knowledge Production | 2014 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-147 | Schreibman, S., Siemens, R. & Unsworth, J. (eds.) | A Companion to Digital Humanities | 2004 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-148 | Borgman, C. L. | Big Data, Little Data, No Data | 2015 | METHODOLOGY | BAJA | — | CANDIDATE |
| SRC-149 | Wilkinson, M. D. et al. | "The FAIR Guiding Principles for Scientific Data Management and Stewardship" | 2016 | METHODOLOGY | MEDIA | — | CANDIDATE |
| SRC-150 | Bender, E. M., Gebru, T., McMillan-Major, A. & Shmitchell | "On the Dangers of Stochastic Parrots" | 2021 | METHODOLOGY | MEDIA | — | CANDIDATE |

## G. Ampliación 2020–2026 (localizadas por búsqueda web en esta sesión, SRC-151–SRC-200)

> Cada fila incluye la fuente usada para confirmar su existencia. Estado
> `IDENTITY_VERIFIED`: se confirmó autor/título/año aproximado por búsqueda
> web; **no** se verificó edición, ISBN/DOI exacto ni contenido. Las filas
> marcadas `(dato por confirmar)` tienen algún metadato que la búsqueda no
> permitió fijar con certeza (autoría de un capítulo, año exacto, editorial):
> deben confirmarse antes de avanzar de estado, nunca completarse por
> inferencia.

| SRC | Autor(es) | Título | Año | Clasificación | PI relacionadas | Fuente de verificación | Estado |
|---|---|---|---|---|---|---|---|
| SRC-151 | Youatt, R. | Interspecies Politics: Nature, Borders, States (Univ. of Michigan Press) | 2020 | STATE_OF_ART | PI-06 | [press.umich.edu](https://press.umich.edu/Books/I/Interspecies-Politics) | IDENTITY_VERIFIED |
| SRC-152 | Chao, S. et al. (eds.) | The Promise of Multispecies Justice (Duke UP) | 2022 | STATE_OF_ART | PI-06 | [read.dukeupress.edu](https://read.dukeupress.edu/books/book/3093/The-Promise-of-Multispecies-Justice) | IDENTITY_VERIFIED |
| SRC-153 | Donaldson, S. & Kymlicka, W. | "Realizing Interspecies Democracy" (Democratic Theory 8/1) | 2021 | STATE_OF_ART | PI-06 | búsqueda web (PhilPapers/citas cruzadas) | IDENTITY_VERIFIED |
| SRC-154 | Donaldson, S. & Kymlicka, W. | "Membership Rights for Animals" (Philosophy, supl. 91) | 2022 | STATE_OF_ART | PI-06 | [willkymlicka.ca](https://willkymlicka.ca/publications/articles-chapters) | IDENTITY_VERIFIED |
| SRC-155 | Donaldson, S. & Kymlicka, W. | "Doing Politics with Animals" (Social Research 90/4) | 2023 | STATE_OF_ART | PI-06 | [willkymlicka.ca](https://willkymlicka.ca/publications/articles-chapters) | IDENTITY_VERIFIED |
| SRC-156 | Donaldson, S., Kymlicka, W. & Janara, L. | "Animal Ghosts at Canadian Universities" (Animals 13(24)) | 2023 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-157 | Kymlicka, W. | "Rethinking Human Rights for a More-than-Human World" (More Than Human Rights, NYU Press) | 2024 | STATE_OF_ART | PI-06 | [willkymlicka.ca](https://willkymlicka.ca/publications/articles-chapters) | IDENTITY_VERIFIED |
| SRC-158 | Garner, R. | "The Case for an Interspecies Theory of Democracy" (Journal of Animal Ethics) | 2022 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-159 | Cochrane, A. & Cojocaru, M.-D. | "Solidarity with Wild Animals" (Ethics, Policy and Environment) | 2023 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-160 | Cochrane, A. | "Cosmozoopolis: The Case Against Group-Differentiated Animal Rights" (dato por confirmar: año) | (por confirmar) | STATE_OF_ART | PI-06 | [PhilPapers](https://philpapers.org/rec/ALACTC-3) | IDENTITY_VERIFIED |
| SRC-161 | Garner, R. | "Animals and Democratic Theory: Beyond an Anthropocentric Account" (dato por confirmar: año) | (por confirmar) | STATE_OF_ART | PI-06 | [PhilPapers](https://philpapers.org/rec/GARAAD-6) | IDENTITY_VERIFIED |
| SRC-162 | Meijer, E. | "Global injustice and animals: towards a multispecies social connection model" | 2023 | STATE_OF_ART | PI-06 | [pure.uva.nl](https://pure.uva.nl/ws/files/169637559/meijer-2023-global-injustice-and-animals-towards-a-multispecies-social-connection-model.pdf) | IDENTITY_VERIFIED |
| SRC-163 | Meijer, E. | "A Daoist-inspired Approach to Multispecies Relations" (Environmental Philosophy) | 2024 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-164 | Meijer, E. | Multispecies Dialogues: Doing Philosophy with Animals, Children, the Sea and Others (Amsterdam UP) | 2025 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-165 | Narayanan, Y. | "Animal-state relations: A critical multispecies geopolitics of animality" | 2025 | STATE_OF_ART | PI-02, PI-06 | [journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/03091325251348611) | IDENTITY_VERIFIED |
| SRC-166 | Narayanan, Y. | "For multispecies liberatory futures: Three principles..." | 2023 | STATE_OF_ART | PI-06 | búsqueda web (doi.org/10.1177/27539687231183449) | IDENTITY_VERIFIED |
| SRC-167 | Narayanan, Y. & Srinivasan, K. | "Theme issue introduction: The species turn in Indian identity politics" | 2023 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-168 | Narayanan, Y. | "Mother Cow, Mother India: A Multispecies Politics of Dairy in India" | 2023/2024 | STATE_OF_ART | PI-06 | [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/2325548X.2023.2277938) | IDENTITY_VERIFIED |
| SRC-169 | Faria, C. | Animal Ethics in the Wild: Wild Animal Suffering and Intervention in Nature (Cambridge UP) | 2022 | STATE_OF_ART | PI-06 | [cambridge.org](https://www.cambridge.org/core/books/animal-ethics-in-the-wild/F9FF5F7415D62DA32C859F581B1E0C8A) | IDENTITY_VERIFIED |
| SRC-170 | Johannsen, K. (ed.) | Positive Duties to Wild Animals (Routledge) | 2024 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-171 | Browning, H. & Veit, W. | "Positive Wild Animal Welfare" (Biology & Philosophy) | 2023 | STATE_OF_ART | PI-06 | [link.springer.com](https://link.springer.com/article/10.1007/s10539-023-09901-5) | IDENTITY_VERIFIED |
| SRC-172 | Horta, O. & Teran, D. | "Reducing Wild Animal Suffering Effectively..." (Ethics, Policy and Environment) | 2023 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-173 | (autor por confirmar) | "Indigenizing wild animal sovereignty" (PMC) | (~2022–2024) | STATE_OF_ART | PI-02, PI-06 | [ncbi.nlm.nih.gov/pmc/articles/PMC10947386](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10947386/) | IDENTITY_VERIFIED |
| SRC-174 | Milburn, J. | Food, Justice, and Animals: Feeding the World Respectfully (Oxford UP) | 2023 | STATE_OF_ART | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-175 | Adams, C. J., Gruen, L. & Crary, A. (eds.) | The Good It Promises, the Harm It Does: Critical Essays on Effective Altruism (Oxford UP) | 2023 | SECONDARY_CORE | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-176 | Fasel, R. N. & Butler, S. C. | Animal Rights Law (Hart Publishing) | 2023 | CONTEXT | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-177 | Adenitire, J. O. & Fasel, R. | Animals and the Constitution (dato por confirmar: año, editorial) | (por confirmar) | CONTEXT | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-178 | Deckha, M. | Animals as Legal Beings (Univ. of Toronto Press) (dato por confirmar: año) | (por confirmar) | CONTEXT | PI-06 | [utppublishing.com](https://utppublishing.com/doi/book/10.3138/9781487525873) | IDENTITY_VERIFIED |
| SRC-179 | Bernet Kempers, E. | What Are Animal Rights For? | 2024 | STATE_OF_ART | PI-06 | [ncbi.nlm.nih.gov/pmc/articles/PMC11418069](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11418069/) | IDENTITY_VERIFIED |
| SRC-180 | Braidotti, R. | Posthuman Feminism (Polity) | 2022 | DEEPENING | PI-04 | búsqueda web | IDENTITY_VERIFIED |
| SRC-181 | Ferrando, F. | The Art of Being Posthuman: Who are we in the 21st century? | 2023 | DEEPENING | PI-04 | búsqueda web | IDENTITY_VERIFIED |
| SRC-182 | Calarco, M. | The Three Ethologies: A Positive Vision for Rebuilding Human-Animal Relationships (Univ. of Chicago Press) | 2024 | DEEPENING | PI-04 | [press.uchicago.edu](https://press.uchicago.edu/ucp/books/book/chicago/T/bo212929943.html) | IDENTITY_VERIFIED |
| SRC-183 | Cimatti, F. & Salzani, C. (eds.) | The Biopolitical Animal (Edinburgh UP) | 2024 | CONTEXT | PI-02, PI-04 | [progressivegeographies.com](https://progressivegeographies.com/2024/11/17/felice-cimatti-and-carlo-salzani-eds-the-biopolitical-animal-edinburgh-university-press-november-2024/) | IDENTITY_VERIFIED |
| SRC-184 | Piskorski, R. | Derrida and Textual Animality: For a Zoogrammatology of Literature (Palgrave) | 2020 | SECONDARY_CORE | PI-04 | búsqueda web | IDENTITY_VERIFIED |
| SRC-186 | (autor por confirmar) | "Jacques Derrida on the Aporias of Hospitality" | 2024 | SECONDARY_CORE | PI-01, PI-05 | [researchgate.net](https://www.researchgate.net/publication/380893056_Jacques_Derrida_on_the_Aporias_of_Hospitality) | IDENTITY_VERIFIED |
| SRC-187 | (autor por confirmar) | "Paradise Lost in Derrida and Agamben: onto-theology of animal life" | 2024 | SECONDARY_CORE | PI-04 | [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/21692327.2024.2439852) | IDENTITY_VERIFIED |
| SRC-188 | Di Cesare, D. | Resident Foreigners: A Philosophy of Migration (Polity) | 2020 | CONTEXT | PI-05 | búsqueda web | IDENTITY_VERIFIED |
| SRC-189 | Lejeune, C., Pagès-El Karoui, D., Schmoll, C. & Thiollet, H. (eds.) | Migration, Urbanity and Cosmopolitanism in a Globalized World (Springer) | 2021 | CONTEXT | PI-05 | [link.springer.com](https://link.springer.com/chapter/10.1007/978-3-030-67365-9_1) | IDENTITY_VERIFIED |
| SRC-190 | Piasentier, M. & Raimondi, S. (eds.) | Debating Biopolitics: New Perspectives on the Government of Life (Edward Elgar) | 2022 | CONTEXT | PI-02 | [michel-foucault.com](https://michel-foucault.com/2023/03/13/marco-piasentier-and-sara-raimondi-debating-biopolitics-new-perspectives-on-the-government-of-life-2022/) | IDENTITY_VERIFIED |
| SRC-191 | Esposito, R. | "Oltre la biopolitica" / "Beyond Biopolitics" (formato por confirmar: ¿libro, conferencia o ensayo?) | 2024 | CONTEXT | PI-02, PI-07 | [michel-foucault.com](https://michel-foucault.com/2024/06/02/roberto-esposito-oltre-la-biopolitica-beyond-biopolitics-2024/) | IDENTITY_VERIFIED |
| SRC-192 | (autor por confirmar) | "Algorithmic Governmentality, Digital Sovereignty, and Agency" (Weizenbaum Journal) | (por confirmar) | METHODOLOGY | PI-02 | [ojs.weizenbaum-institut.de](https://ojs.weizenbaum-institut.de/index.php/wjds/article/view/87/80) | IDENTITY_VERIFIED |
| SRC-193 | (autor por confirmar) | "Algorithmic sovereignty and democratic resilience: rethinking AI governance in the age of generative AI" (AI and Ethics, Springer) | 2025 | METHODOLOGY | PI-02 | [link.springer.com](https://link.springer.com/article/10.1007/s43681-025-00739-z) | IDENTITY_VERIFIED |
| SRC-194 | (autor por confirmar) | "Reproducibility and explainability in digital humanities" (Intl. Journal of Digital Humanities, Springer) | 2023 | METHODOLOGY | — | [link.springer.com](https://link.springer.com/article/10.1007/s42803-023-00083-w) | IDENTITY_VERIFIED |
| SRC-195 | (autor por confirmar) | "Reproducibility, verifiability, and computational historical research" (Intl. Journal of Digital Humanities, Springer) | 2023 | METHODOLOGY | — | [link.springer.com](https://link.springer.com/article/10.1007/s42803-023-00068-9) | IDENTITY_VERIFIED |
| SRC-196 | Kymlicka, W. (entrevista) | "Will Kymlicka on Animal Denizens and Foreigners in the Wilderness" (GBS Schweiz; fuente divulgativa, no académica revisada por pares) | (por confirmar) | STATE_OF_ART | PI-06 | [gbs-schweiz.org](https://gbs-schweiz.org/blog/will-kymlicka-on-animal-denizens-and-foreigners-in-the-wilderness-interview-part-2/) | IDENTITY_VERIFIED |
| SRC-197 | Innu Council of Ekuanitshit & Minganie RCM | Resoluciones de personalidad jurídica del río Magpie (Québec) — desarrollo jurídico, no fuente filosófica; relevante como caso de estudio | 2021 | CONTEXT | PI-06 | búsqueda web (Columbia/Sabin Center y prensa especializada) | IDENTITY_VERIFIED |
| SRC-198 | Corte Constitucional de Ecuador | Sentencia sobre el bosque Los Cedros (derechos de la naturaleza) — caso, no fuente filosófica | 2021 | CONTEXT | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-199 | España — Ley del Mar Menor | Personalidad jurídica del Mar Menor — caso, no fuente filosófica | 2022 | CONTEXT | PI-06 | búsqueda web | IDENTITY_VERIFIED |
| SRC-200 | Corte de Justicia de Perú (caso Kukama / Canaquiri Murayari) | Personalidad jurídica del río Marañón — caso, no fuente filosófica | 2024 | CONTEXT | PI-06 | búsqueda web | IDENTITY_VERIFIED |

## Duplicados y observaciones de calidad ya detectados

- **SRC-037** es el único registro canónico de Naas, *Threshold Phenomena*.
  El duplicado histórico `SRC-185` fue retirado durante la migración; no debe
  reutilizarse como una segunda clave para la misma obra.
- SRC-197–SRC-200 no son fuentes filosóficas sino desarrollos jurídicos
  (personalidad jurídica de ríos y ecosistemas). Se registran aquí porque son
  directamente pertinentes al eje C (comunidad política interespecie) como
  **casos**, no como bibliografía a citar del mismo modo que un libro o
  artículo; si se incorporan, deberían tratarse con la plantilla de caso que
  el investigador decida, no como entrada de `bibliography.bib`.
- Las filas marcadas `(autor por confirmar)` o `(dato por confirmar)` no
  deben completarse por inferencia ni por plausibilidad. Permanecen así
  hasta que el investigador (o una verificación posterior explícitamente
  solicitada) las confirme contra la fuente primaria del dato.

## Próximo paso recomendado

No es crear 200 fichas (`templates/ficha-fuente.md`) de una vez — eso
recrearía exactamente el problema que `governance/decision-log.md` (DEC-003)
identificó en las ramas de PR históricas #2 y #9 (bibliotecas especulativas).
El siguiente paso es que el investigador seleccione, de la columna
`PRIORIDAD: ALTA`, la primera obra que realmente va a leer, verifique su
edición exacta, y solo entonces se cree su entrada en `bibliography.bib` y su
ficha en `research/sources/notes/`.

## Previous research by author

This class is archival background, not part of the doctoral source corpus. It is
kept here so that one machine-readable source identifier has one canonical
category and reading stage; explanatory limitations remain in the archival files.

| ID | Work | Category | Reading stage | Bibliographic key |
|---|---|---|---|---|
| SRC-PR-001 | Valderrama Pino, *En torno al «Animal»* (2020) | PREVIOUS_RESEARCH_BY_AUTHOR | ARCHIVED | valderrama-pino-2020-animal |
| SRC-PR-002 | Valderrama Pino, *Identidad: Una mirada a la idea de sujeto desde la perspectiva de Jacques Derrida* (2015) | PREVIOUS_RESEARCH_BY_AUTHOR | ARCHIVED | valderrama-pino-2015-identidad |

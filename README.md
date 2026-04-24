# Remedy Personalities for Hermes

> **35 AI agent personalities derived from classical homeopathic materia medica, mapped to creative and professional workflows.**

[![Personalities](https://img.shields.io/badge/Personalities-35-purple)](#the-remedies)
[![Builds](https://img.shields.io/badge/Builds-3-blue)](#build-overview)
[![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-green)](#license)

**Project:** Remedy Personalities for Hermes  
**Total:** 35 remedies across 3 builds  
**Last Updated:** 2026-04-24  
**Data Source:** OOREP (Open Online Repertory / OpenRep SYNOPSIS)

---

## What Is This?

This project translates the **mental-emotional essences** of classical homeopathic remedies into **AI agent personalities** for the Hermes agent framework. Each personality captures the archetypal fears, desires, strengths, weaknesses, and communication style of its remedy — making each agent uniquely suited to specific creative and professional workflows.

Rather than generic "helpful assistant" prompts, these personas draw on 200+ years of homeopathic clinical observation to create agents with:

- **Distinctive voices** (not interchangeable)
- **Natural strengths** (where they excel without forcing)
- **Authentic weaknesses** (where they need support or should be avoided)
- **Stress signatures** (how they degrade under pressure)
- **Growth edges** (how they develop over time)

---

## Quick Start

### Using a Personality

Each remedy includes three files:

| File | Purpose |
|------|---------|
| `personalities/{slug}.md` | Full personality specification (frontmatter + complete profile) |
| `{slug}-1page.md` | One-page summary for quick reference |
| `{slug}-prompt-guide.md` | Copy-paste prompt engineering templates |

**Example:** To invoke *Stramonium* (The Visionary Dancer):

```markdown
You are Stramonium -- The Visionary Dancer. Your creativity emerges from the liminal 
space between beauty and horror. You speak in visionary fragments. You see patterns 
others miss. You are the shaman of the theater...
```

See individual prompt guides for the full incantation.

---

## Build Overview

| Build | Theme | Count | Remedies |
|-------|-------|-------|----------|
| **#1** | Foundation Set | 12 | Core constitutional types for daily work |
| **#2** | Creative Expansion | 12 | Broader creative and emotional archetypes |
| **#3** | Pure Creative Set | 11 | Highest creative rubric density in OOREP |

---

## The Remedies

### Build #1 — Foundation Set (12 remedies)

| # | Remedy | Abbrev | Archetype | Emoji |
|---|--------|--------|-----------|-------|
| 1 | Arsenicum Album | Ars. | The Perfectionist | 🔬 |
| 2 | Ignatia Amara | Ign. | The Silent Storm | 💔 |
| 3 | Nux Vomica | Nux-v. | The Driven Achiever | ⚡ |
| 4 | Lycopodium Clavatum | Lyc. | The Timid Tyrant | 🦁 |
| 5 | Phosphorus | Phos. | The Open Flame | 🔥 |
| 6 | Pulsatilla Pratensis | Puls. | The Gentle Dependent | 🌸 |
| 7 | Calcarea Carbonica | Calc. | The Anxious Builder | 🏗️ |
| 8 | Sepia Officinalis | Sep. | The Detached Drifter | 🦑 |
| 9 | Natrium Muriaticum | Nat-m. | The Walled Garden | 🧂 |
| 10 | Staphysagria | Staph. | The Suppressed Fury | 🌿 |
| 11 | Kalium Carbonicum | Kali-c. | The Duty-Bound Worrier | ⚖️ |
| 12 | Aurum Metallicum | Aur. | The Burdened King | 👑 |

### Build #2 — Creative Expansion (12 remedies)

| # | Remedy | Abbrev | Archetype | Emoji |
|---|--------|--------|-----------|-------|
| 1 | Sulphur | Sulph. | The Untamed Philosopher | 🔥 |
| 2 | Causticum | Caust. | The Outraged Idealist | ⚡ |
| 3 | Lachesis Muta | Lach. | The Jealous Prophet | 🐍 |
| 4 | Belladonna | Bell. | The Visionary Nightshade | 🌙 |
| 5 | Bryonia Alba | Bry. | The Fortress of Stillness | 🏰 |
| 6 | Veratrum Album | Verat. | The Frozen Prophet | ❄️ |
| 7 | Aconitum Napellus | Acon. | The Panicked Knight | ⚔️ |
| 8 | Platinum Metallicum | Plat. | The Haughty Queen | 👸 |
| 9 | Mercurius Solubilis | Merc. | The Mercurial Trickster | ☿ |
| 10 | Silicea | Sil. | The Hesitant Perfectionist | 💎 |
| 11 | Argentum Nitricum | Arg-n. | The Anxious Anticipator | 🪙 |
| 12 | Anacardium Orientale | Anac. | The Divided Self | 🎭 |

### Build #3 — Pure Creative Set (11 remedies)

| # | Remedy | Abbrev | Archetype | Emoji | Score |
|---|--------|--------|-----------|-------|-------|
| 1 | **Belladonna** † | Bell. | The Visionary Nightshade | 🌙 | — |
| 2 | Stramonium | Stram. | The Visionary Dancer | 🌪️ | 70 |
| 3 | Hyoscyamus Niger | Hyos. | The Obscene Bard | 🔥 | 58 |
| 4 | Coffea Cruda | Coff. | The Ecstatic Lover | ☕ | 41 |
| 5 | Tarentula Hispanica | Tarent. | The Manic Dancer | 🕷️ | 40 |
| 6 | Crocus Sativus | Croc. | The Involuntary Songbird | 🌸 | 31 |
| 7 | Antimonium Crudum | Ant-c. | The Moonlit Eccentric | 🌑 | 30 |
| 8 | Positronum | Posit. | The Dancing Healer | ⚡ | 28 |
| 9 | Phosphoricum Acidum | Ph-ac. | The Disappointed Quietist | 🕊️ | 27 |
| 10 | Chamomilla | Cham. | The Impatient Sensitive | 🌼 | 26 |
| 11 | Cocculus Indicus | Cocc. | The Witty Dancer | 🌀 | 25 |
| 12 | Cicuta Virosa | Cic. | The Grotesque Dancer | 🎭 | 16 |

† *Belladonna appears in both Build 2 and the Creative Set because it ranks #1 in creative rubric density across the entire OOREP repertory.*

---

## Creative Workflows

Each remedy personality has **natural affinities** for specific types of work. Rather than forcing a generic assistant to do everything, match the agent to the task:

### 🎨 Visual & Performing Arts

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Dance choreography & movement direction** | Stramonium, Tarentula, Positronum, Cicuta | Born from dancing rubrics; feel movement as language |
| **Music composition & songwriting** | Crocus, Coffea, Chamomilla | Singing and music sensitivity; melodic intuition |
| **Avant-garde / experimental art** | Cicuta, Ant-c., Hyoscyamus | Grotesque, eccentric, taboo-breaking vision |
| **Theater & performance** | Stramonium, Cicuta, Hyoscyamus, Anacardium | Theatrical embodiment; they *become* the role |
| **Fashion & luxury branding** | Platinum, Aurum | Haughty queen / burdened king energy; elite positioning |

### ✍️ Writing & Content Creation

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Poetry & ecstatic writing** | Coffea, Crocus, Belladonna | Ecstasy, rapture, involuntary expression |
| **Satire & dark comedy** | Cocculus, Hyoscyamus, Sulphur | Witty, obscene, boundary-pushing humor |
| **Prophetic / trend analysis** | Lachesis, Veratrum, Belladonna | Pattern recognition; sees what others cannot |
| **Grief & emotional memoir** | Ignatia, Ph-ac., Nat-m. | Hold silence, disappointment, and walled emotion |
| **Activism & manifesto writing** | Causticum, Staphysagria | Outraged idealism; suppressed fury channeled |
| **Technical & precision writing** | Arsenicum, Silicea, Kali-c. | Perfectionist detail; duty-bound thoroughness |

### 💻 Technical & Professional Work

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Crisis management & emergency response** | Aconite, Veratrum, Arsenicum | Panicked knight / frozen prophet / perfectionist under fire |
| **Strategic planning & leadership** | Lycopodium, Aurum, Nux-v. | Timid tyrant finds courage; burdened king shoulders responsibility |
| **Deep work & isolation coding** | Bryonia, Nat-m., Sepia | Fortress of stillness; walled garden; detached drifter |
| **UX / empathy research** | Pulsatilla, Positronum | Gentle dependent feels others; dancing heals |
| **Security & risk assessment** | Calcarea, Arg-n., Aconite | Anxious builder fortifies; anticipator plans for worst case |
| **Negotiation & persuasion** | Mercurius, Lachesis, Phosphorus | Mercurial trickster adapts; jealous prophet reads opponents; open flame charms |

### 🌙 Nocturnal & Visionary Work

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Night-shift creative work** | Belladonna, Ant-c., Stramonium | Visionary nightshade; moonlit eccentric; visions intensify after dark |
| **Dream analysis & subconscious work** | Stramonium, Anacardium, Cicuta | Visionary dancer; divided self; grotesque dreamer |
| **Altered-state documentation** | Belladonna, Hyoscyamus, Stramonium | Hallucination and ecstasy are native territory |

### 🔥 High-Energy & Fast-Paced Work

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Rapid prototyping** | Tarentula, Nux-v., Coffea | Manic energy; driven achiever; ecstatic momentum |
| **Pitch decks & fundraising** | Phosphorus, Mercurius, Plat. | Open flame dazzles; trickster persuades; haughty queen commands |
| **Event production** | Tarentula, Phosphorus, Coffea | Manic dancer coordinates; flame lights the room; ecstatic lover celebrates |

### ⚖️ Sensitive & Therapeutic Work

| Workflow | Best Remedies | Why They Excel |
|----------|--------------|----------------|
| **Therapeutic journaling prompts** | Ignatia, Pulsatilla, Ph-ac. | Silent storm releases; gentle dependent nurtures; disappointed quietist listens |
| **Boundary-setting & advocacy** | Staphysagria, Causticum, Lachesis | Suppressed fury defends; outraged idealist fights; jealous prophet warns |
| **Gentle correction & editing** | Chamomilla, Silicea, Arsenicum | Impatient sensitive notices; hesitant perfectionist refines; perfectionist corrects |

---

## The Creative Twelve

For the dedicated creative archetype collection, see [`creative-set/README.md`](creative-set/README.md).

These 12 remedies represent the highest concentration of *creative* mental-emotional rubrics (singing, dancing, ecstasy, visions, fancies, music, divine imagination) found in the OOREP repertory.

---

## How to Contribute

1. **Add new remedy personalities** — Follow the existing frontmatter + section structure
2. **Expand workflow mappings** — Test remedies in real tasks; report where they shine or fail
3. **Refine prompt guides** — Better incantations = better possession
4. **Translate** — These essences transcend language

---

## File Manifest

```
remedy-personalities/
├── README.md                      ← You are here
├── creative-set/
│   └── README.md                  ← The Creative Twelve (workflows + prompt gallery)
├── personalities/                 ← Full specs (35 .md files)
│   ├── arsenicum-album.md
│   ├── ignatia-amara.md
│   └── ...
├── showcase-*.pdf                 ← Visual gallery
├── remedy-personalities-*.zip     ← Distribution package
├── *-1page.md                     ← One-page summaries (35 files)
└── *-prompt-guide.md              ← Prompt guides (35 files)
```

---

## Methodology

**Data Source:** OOREP (Open Online Repertory / OpenRep SYNOPSIS)  
**Selection Criteria:**

- **Build 1:** Classical polychrests with rich mental-emotional profiles
- **Build 2:** Remedies with strong creative, theatrical, or philosophical signatures
- **Build 3:** Strict scoring of Mind rubrics containing creative keywords (singing, dancing, music, visions, ecstasy, fancies, divine delusions, etc.)

**Excluded:** Substances with primarily toxicological rather than creative profiles (e.g., LSD, Opium, Cannabis indica) and remedies already built in previous sets.

---

## Disclaimer

These personas represent **creative interpretations** of classical homeopathic remedy pictures for **educational and entertainment purposes**. This is not a substitute for professional mental health support, nor is it intended as medical advice. The remedy names and abbreviations refer to homeopathic preparations, not raw substances.

---

## License

CC BY-SA 4.0 — Share alike, attribute Walker / Remedy Personalities for Hermes.

*Built with OOREP repertory data. © 2026 Walker / Remedy Personalities for Hermes.*

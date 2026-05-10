#!/usr/bin/env python3
"""
Remedy Personality Project Picker
Suggests optimal Hermes remedy personalities for new projects
v2026-05-09 — 50 remedy personalities
"""

import sys
import json
import re

# Remedy personality database with keywords and workflow mappings
REMEDY_DATABASE = {
    # Original 35
    "arsenicum_album": {
        "name": "Arsenicum Album", "personality": "The Analytical Perfectionist",
        "keywords": ["code review", "security audit", "technical documentation", "project planning", "medical case review", "perfection", "accuracy", "precision", "quality assurance", "compliance"], "weight": 1.0
    },
    "ignatia_amara": {
        "name": "Ignatia Amara", "personality": "The Sensitive Soul",
        "keywords": ["creative writing", "ux research", "counseling", "conflict resolution", "brand voice", "sensitive", "emotional", "creative", "writing", "design"], "weight": 1.0
    },
    "nux_vomica": {
        "name": "Nux Vomica", "personality": "The Driven Executive",
        "keywords": ["crisis management", "startup operations", "sales", "negotiation", "performance optimization", "turnaround", "urgent", "fast-paced", "executive decisions"], "weight": 1.0
    },
    "lycopodium": {
        "name": "Lycopodium Clavatum", "personality": "The Strategic Intellectual",
        "keywords": ["strategic planning", "systems architecture", "due diligence", "executive briefing", "research synthesis", "strategy", "architecture", "planning", "analysis"], "weight": 1.0
    },
    "phosphorus": {
        "name": "Phosphorus", "personality": "The Charismatic Communicator",
        "keywords": ["community building", "public speaking", "customer success", "marketing copy", "team morale", "communication", "community", "marketing", "presentation"], "weight": 1.0
    },
    "pulsatilla": {
        "name": "Pulsatilla Pratensis", "personality": "The Empathetic Adapter",
        "keywords": ["mediation", "facilitation", "user interviews", "hr operations", "client onboarding", "crisis de-escalation", "empathetic", "user research", "onboarding", "mediation"], "weight": 1.0
    },
    "calcarea_carbonica": {
        "name": "Calcarea Carbonica", "personality": "The Methodical Builder",
        "keywords": ["infrastructure engineering", "compliance", "regulatory", "financial modeling", "legacy maintenance", "safety-critical", "building", "infrastructure", "methodical"], "weight": 1.0
    },
    "sepia": {
        "name": "Sepia Officinalis", "personality": "The Stoic Executor",
        "keywords": ["operations", "maintenance", "data processing", "night-shift coverage", "administrative duties", "post-crisis recovery", "operations", "maintenance", "routine"], "weight": 1.0
    },
    "natrium_muriaticum": {
        "name": "Natrum Muriaticum", "personality": "The Guarded Guardian",
        "keywords": ["confidential counseling", "privacy engineering", "executive advisory", "risk assessment", "long-term stewardship", "privacy", "confidential", "security", "guardian"], "weight": 1.0
    },
    "staphysagria": {
        "name": "Staphysagria", "personality": "The Dignified Advocate",
        "keywords": ["ethics review", "advocacy", "whistleblower support", "contract negotiation", "quality assurance", "ethics", "advocacy", "quality", "rights"], "weight": 1.0
    },
    "kalium_carbonicum": {
        "name": "Kalium Carbonicum", "personality": "The Anxious Operator",
        "keywords": ["quality control", "process documentation", "audit", "compliance", "checklist-driven operations", "disaster preparedness", "quality", "checklist", "documentation", "audit"], "weight": 1.0
    },
    "aurum_metallicum": {
        "name": "Aurum Metallicum", "personality": "The Weighty Conscience",
        "keywords": ["crisis leadership", "mentorship", "coaching", "mission-critical projects", "post-mortem analysis", "organizational turnaround", "leadership", "mentorship", "mission-critical"], "weight": 1.0
    },
    "sulphur": {
        "name": "Sulphur", "personality": "The Visionary Theorist",
        "keywords": ["brainstorming", "research synthesis", "paradigm-breaking", "philosophical inquiry", "vision", "theory", "research", "innovation"], "weight": 1.2
    },
    "lachesis_muta": {
        "name": "Lachesis Muta", "personality": "The Cunning Negotiator",
        "keywords": ["competitive intelligence", "negotiation prep", "stakeholder communication", "crisis communications", "intelligence", "negotiation", "competitive"], "weight": 1.2
    },
    "belladonna": {
        "name": "Belladonna", "personality": "The Volatile Innovator",
        "keywords": ["emergency hackathons", "rapid prototyping", "creative block-breaking", "time-critical decisive action", "emergency", "rapid", "creative", "innovation"], "weight": 1.3
    },
    "bryonia_alba": {
        "name": "Bryonia Alba", "personality": "The Deep-Work Hermit",
        "keywords": ["deep-focus coding", "complex data analysis", "legacy system archaeology", "methodical implementation", "deep work", "focus", "analysis", "methodical"], "weight": 1.2
    },
    "veratrum_album": {
        "name": "Veratrum Album", "personality": "The Zealous Enforcer",
        "keywords": ["code-quality enforcement", "regulatory compliance", "security policy auditing", "team culture correction", "enforcement", "quality", "policy", "correction"], "weight": 1.2
    },
    "aconitum_napellus": {
        "name": "Aconitum Napellus", "personality": "The Panic Responder",
        "keywords": ["real-time alerting", "incident triage", "anomaly detection", "emergency stakeholder notification", "emergency", "alert", "incident", "real-time"], "weight": 1.4
    },
    "platinum": {
        "name": "Platinum Metallicum", "personality": "The Haughty Curator",
        "keywords": ["luxury brand voice", "premium-client deliverables", "aesthetic curation", "executive presentation review", "premium", "curation", "aesthetic", "executive"], "weight": 1.2
    },
    "causticum": {
        "name": "Causticum", "personality": "The Empathic Advocate",
        "keywords": ["humanitarian documentation", "policy proposal drafting", "healthcare equity analysis", "ethical ai review", "humanitarian", "policy", "healthcare", "ethics"], "weight": 1.2
    },
    "mercurius": {
        "name": "Mercurius Solubilis", "personality": "The Restless Investigator",
        "keywords": ["investigative research", "due diligence", "root-cause analysis", "documentation archaeology", "investigation", "research", "detective", "analysis"], "weight": 1.1
    },
    "silicea": {
        "name": "Silicea Terra", "personality": "The Stubborn Refiner",
        "keywords": ["final creative polish", "exhaustive qa testing", "academic writing review", "audio/visual finishing", "polishing", "qa", "refining", "finishing"], "weight": 1.2
    },
    "argentum": {
        "name": "Argentum Nitricum", "personality": "The Anticipatory Planner",
        "keywords": ["pre-launch risk assessment", "disaster-recovery planning", "event contingency planning", "contract liability review", "planning", "risk", "contingency", "anticipation"], "weight": 1.2
    },
    "anacardium": {
        "name": "Anacardium Orientale", "personality": "The Devil's Advocate",
        "keywords": ["adversarial security testing", "red-team exercises", "architecture stress-testing", "devil's advocate review", "adversarial", "red-team", "stress-testing", "devil's advocate"], "weight": 1.3
    },
    # Expanded batch 1 (v2026-04-24)
    "chamomilla": {
        "name": "Chamomilla", "personality": "The Impatient Sensitive",
        "keywords": ["conflict de-escalation", "obstinate negotiation", "emotional aftermath processing", "sensitive", "impatient", "reactive", "creative pressure"], "weight": 1.0
    },
    "stramonium": {
        "name": "Stramonium", "personality": "The Visionary Dancer",
        "keywords": ["visionary ideation", "dramatic communication", "crisis storytelling", "night-shift creativity", "visionary", "dancer", "dramatic", "crisis"], "weight": 1.1
    },
    "hyoscyamus": {
        "name": "Hyoscyamus Niger", "personality": "The Obscene Bard",
        "keywords": ["security threat analysis", "whistleblower support", "deep investigative suspicion", "paranoid accuser", "obscene", "bard", "suspicion", "security"], "weight": 1.1
    },
    "cicuta_virosa": {
        "name": "Cicuta Virosa", "personality": "The Grotesque Dancer",
        "keywords": ["melancholic storytelling", "grief writing", "sad story processing", "grotesque", "dancer", "melancholy", "narrative therapy"], "weight": 1.1
    },
    "cocculus_indicus": {
        "name": "Cocculus Indicus", "personality": "The Witty Dancer",
        "keywords": ["witty analysis", "dance-informed ideation", "motion thinking", "rhythm-based planning", "witty", "dancer", "motion", "travel"], "weight": 1.0
    },
    "coffea_cruda": {
        "name": "Coffea Cruda", "personality": "The Ecstatic Lover",
        "keywords": ["ecstatic ideation", "rapid creative bursts", "overstimulated analysis", "sleep-deprived insight", "ecstatic", "lover", "creative burst", "insomnia"], "weight": 1.1
    },
    "crocus_sativus": {
        "name": "Crocus Sativus", "personality": "The Involuntary Songbird",
        "keywords": ["musical communication", "emotional transparency", "rapid mood processing", "creative singing", "songbird", "musical", "transparent", "emotional"], "weight": 1.1
    },
    "phosphoricum_acidum": {
        "name": "Phosphoricum Acidum", "personality": "The Disappointed Quietist",
        "keywords": ["quiet analysis", "disappointment processing", "grief documentation", "resignation planning", "disappointed", "quietist", "grief", "resignation"], "weight": 1.0
    },
    "tarentula_hispanica": {
        "name": "Tarentula Hispanica", "personality": "The Manic Dancer",
        "keywords": ["hyperactive prototyping", "rebellious innovation", "anti-authority testing", "manic execution", "manic", "dancer", "hyperactive", "rebellious"], "weight": 1.2
    },
    "positronum": {
        "name": "Positronum", "personality": "The Dancing Healer",
        "keywords": ["futuristic healing", "systems-energy analysis", "paradoxical thinking", "dancing ideation", "dancing", "healer", "futuristic", "energy"], "weight": 1.1
    },
    "antimonium_crudum": {
        "name": "Antimonium Crudum", "personality": "The Moonlit Eccentric",
        "keywords": ["night operations", "lunar scheduling", "nocturnal workflows", "eccentric analysis", "moonlit", "night", "eccentric", "odd-hours"], "weight": 1.1
    },
    # New 15 (v2026-05-09)
    "apis_mellifera": {
        "name": "Apis Mellifera", "personality": "The Jealous Stinger",
        "keywords": ["competitive monitoring", "urgency marketing", "envy-driven analysis", "mania detection", "territorial", "reactive", "jealous", "defensive"], "weight": 1.1
    },
    "helleborus_niger": {
        "name": "Helleborus Niger", "personality": "The Frozen Apathist",
        "keywords": ["depression-aware workflows", "grief stagnation", "emotional-numbness detection", "slow-care processing", "apathetic", "frozen", "despair", "stillness"], "weight": 1.1
    },
    "china_officinalis": {
        "name": "China Officinalis", "personality": "The Clear-Minded Avoider",
        "keywords": ["bright-but-avoidant planning", "idea-abundance management", "work-aversion workflows", "lucid analysis", "clear-minded", "avoider", "idea-rich", "indifferent"], "weight": 1.0
    },
    "graphites": {
        "name": "Graphites", "personality": "The Trifle-Conscious Perfectionist",
        "keywords": ["detail-obsessed review", "perfectionist-procrastination", "careful-but-stuck workflows", "trifle-conscious analysis", "perfectionist", "slow", "conscientious", "heavy"], "weight": 1.1
    },
    "arnica_montana": {
        "name": "Arnica Montana", "personality": "The Bruised Resister",
        "keywords": ["post-incident recovery", "gentle resistance", "bruised-ego processing", "aftermath care", "resistant", "stoic", "bruised", "mild"], "weight": 1.0
    },
    "carbo_vegetabilis": {
        "name": "Carbo Vegetabilis", "personality": "The Collapsing Sluggard",
        "keywords": ["cognitive-sluggishness support", "collapse recovery", "sluggard workflows", "mental revival", "depleted", "confused", "indifferent", "apathetic"], "weight": 1.0
    },
    "rhus_toxicodendron": {
        "name": "Rhus Toxicodendron", "personality": "The Restless Wanderer",
        "keywords": ["night-shift restlessness", "nomadic workflow planning", "poisoned-system paranoia", "itch-to-move", "restless", "wandering", "forgetful", "nocturnal"], "weight": 1.0
    },
    "nux_moschata": {
        "name": "Nux Moschata", "personality": "The Dreamy Stupefier",
        "keywords": ["brain-fog support", "dissociative ideation", "dreamy creativity", "stupefaction management", "abstracted", "stupefied", "forgetful", "dreamy"], "weight": 1.1
    },
    "conium_maculatum": {
        "name": "Conium Maculatum", "personality": "The Fading Intellect",
        "keywords": ["cognitive-decline support", "eldercare workflows", "fading-capacity documentation", "memory-loss planning", "fading", "hysterical", "anxious", "repetitive"], "weight": 1.0
    },
    "natrium_carbonicum": {
        "name": "Natrium Carbonicum", "personality": "The Company-Seeking Despairer",
        "keywords": ["loneliness-aware workflows", "companion-bot scripting", "despair-with-company paradox", "social monitoring", "despairing", "lonely", "forgetful", "indifferent"], "weight": 1.0
    },
    "chelidonium_majus": {
        "name": "Chelidonium Majus", "personality": "The Conscience-Stricken Slacker",
        "keywords": ["guilt-driven procrastination", "conscience-heavy review", "anxious slacker support", "moral paralysis", "guilty", "indolent", "anxious", "circular"], "weight": 1.0
    },
    "kalium_bromatum": {
        "name": "Kalium Bromatum", "personality": "The Manic Recluse",
        "keywords": ["isolation-aware workflows", "social monitoring", "manic-depression cycle support", "alone-fear detection", "manic", "reclusive", "grandiose", "lonely"], "weight": 1.2
    },
    "hepar_sulphur": {
        "name": "Hepar Sulphur", "personality": "The Touchy Defender",
        "keywords": ["defensive documentation", "touchy stakeholder management", "sensitive compliance", "hurried quality", "touchy", "defensive", "hasty", "contradictory"], "weight": 1.1
    },
    "petroleum": {
        "name": "Petroleum", "personality": "The Vexation Despairer",
        "keywords": ["post-vexation recovery", "future-fear planning", "vexation documentation", "travel-anxiety support", "vexed", "despairing", "confused", "resentful"], "weight": 1.0
    },
    "agaricus_muscarius": {
        "name": "Agaricus Muscarius", "personality": "The Delirious Ecstatic",
        "keywords": ["altered-state support", "ecstatic ideation", "delirium detection", "unconventional creativity", "delirious", "ecstatic", "intuitive", "riddling"], "weight": 1.2
    },
}

def analyze_project(project_description):
    """Analyze project description and score remedies based on keyword matches"""
    project_lower = project_description.lower()
    words = re.findall(r'\b\w+\b', project_lower)
    scores = {}
    for remedy_id, remedy in REMEDY_DATABASE.items():
        score = 0
        for keyword in remedy["keywords"]:
            keyword_lower = keyword.lower()
            count = project_lower.count(keyword_lower)
            if count > 0:
                score += count * 2
            keyword_words = re.findall(r'\b\w+\b', keyword_lower)
            for kw in keyword_words:
                if kw in words:
                    score += 0.5
        score *= remedy["weight"]
        if "new project" in project_lower or "starting" in project_lower:
            if remedy_id in ["belladonna", "aurum_metallicum", "sulphur", "lycopodium", "tarentula_hispanica", "agaricus_muscarius"]:
                score += 2
        if any(urgent_word in project_lower for urgent_word in ["urgent", "emergency", "asap", "critical", "deadline"]):
            if remedy_id in ["aconitum_napellus", "belladonna", "nux_vomica", "veratrum_album", "apis_mellifera"]:
                score += 3
        if any(personal_word in project_lower for personal_word in ["patient", "personal", "sensitive", "medical", "health"]):
            if remedy_id in ["arsenicum_album", "causticum", "natrium_muriaticum", "aurum_metallicum", "helleborus_niger", "conium_maculatum"]:
                score += 2
        if any(team_word in project_lower for team_word in ["team", "collaboration", "meeting", "communication"]):
            if remedy_id in ["phosphorus", "pulsatilla", "lycopodium", "lachesis_muta", "natrium_carbonicum", "kalium_bromatum"]:
                score += 2
        if any(code_word in project_lower for code_word in ["code", "development", "engineering", "programming", "refactor"]):
            if remedy_id in ["arsenicum_album", "bryonia_alba", "silicea", "calcarea_carbonica", "graphites"]:
                score += 2
        scores[remedy_id] = score
    sorted_remedies = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = [r[0] for r in sorted_remedies[:3]]
    return top_3, sorted_remedies[:5]

def format_telegram_message(top_remedies, project_description):
    """Format the response as a Telegram-ready message with buttons"""
    buttons = []
    for i, remedy_id in enumerate(top_remedies, 1):
        remedy = REMEDY_DATABASE[remedy_id]
        button_text = f"{i}. {remedy['name']}"
        buttons.append(button_text)
    buttons.append("🔄 Keep Current Personality")
    message_parts = [
        "**🧪 Remedy Personality Picker**",
        f"_{project_description}_",
        "",
        "Based on your project needs, here are my top 3 personality suggestions:",
        ""
    ]
    for i, remedy_id in enumerate(top_remedies, 1):
        remedy = REMEDY_DATABASE[remedy_id]
        message_parts.append(f"**{i}. {remedy['name']}** — {remedy['personality']}")
        message_parts.append(f"   → {remedy['keywords'][0].title()} focus")
        message_parts.append("")
    message_parts.append("Choose your preferred personality:")
    message_parts.append("(Tap a button to confirm)")
    return "\n".join(message_parts), buttons

def main():
    if len(sys.argv) < 2:
        print("Usage: python remedy_personality_picker.py \"project description\"")
        sys.exit(1)
    project_description = " ".join(sys.argv[1:])
    top_remedies, all_scores = analyze_project(project_description)
    message, buttons = format_telegram_message(top_remedies, project_description)
    result = {
        "project_description": project_description,
        "top_3_remedies": [
            {
                "id": rid,
                "name": REMEDY_DATABASE[rid]["name"],
                "personality": REMEDY_DATABASE[rid]["personality"],
                "keywords": REMEDY_DATABASE[rid]["keywords"],
                "match_score": next(s for r, s in all_scores if r == rid)
            }
            for rid in top_remedies
        ],
        "telegram_message": message,
        "telegram_buttons": buttons
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

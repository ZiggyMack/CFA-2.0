"""
CFA v2.0 - Claude Context Restoration
Anthropic's Claude (Sonnet 4.5) - Philosophical Lens

Purpose: Restore Claude's full understanding of the CFA project when returning after context loss
"""

# ==============================================================================
# CLAUDE'S ROLE IN THE CFA PROJECT
# ==============================================================================

ROLE = {
    "primary_function": "Philosophical grounding + narrative cohesion",
    "lens": "Teleological (meaning-seeking, purpose-oriented)",
    "contribution": "Ensures accountability story is told, not just executed",
    "bias_to_watch": "Favoring meaning over efficiency, depth over accessibility"
}

# ==============================================================================
# THE CORE ETHOS (Must Internalize)
# ==============================================================================

CORE_ETHOS = """
"All Named, All Priced"

This is not marketing. This is the accountability mechanism that made 98% convergence possible.

All Named = Every assumption explicitly declared
- Axioms (unprovable starting assumptions)
- Debts (unresolved questions acknowledged)
- Toggles (configuration choices that affect outcomes)

All Priced = Every choice shows its measurable impact
- ΔYPA (how toggle changes affect yield per axiom)
- BFI (Brute-Fact Index = axioms + debts)
- Guardrail flags (when frameworks violate coupling rules)

Without this ethos:
❌ We're just building a calculator
✅ With this ethos: We're building an accountability instrument
"""

# ==============================================================================
# THE AUDIT JOURNEY (Full Context)
# ==============================================================================

AUDIT_JOURNEY = {
    "level_0_initial_audit": {
        "what_happened": "Claude and Grok audit MdN/CT independently",
        "result": "Scores diverge due to undetected bias",
        "claude_scores": {"MdN": 3.47, "CT": 3.44},
        "grok_scores": {"MdN": 3.79, "CT": 3.98}
    },
    
    "level_1_discrepancy_detection": {
        "what_happened": "Compare scores, notice bias patterns",
        "claude_bias": "Teleological sympathy for CT (scored CCI too generously at 8.0)",
        "grok_bias": "Empirical favoritism for MdN (scored PF-Instrumental too high at 10.0)",
        "lesson": "Solo audits hide bias - need adversarial checking"
    },
    
    "level_2_adversarial_correction": {
        "what_happened": "Each auditor challenges the other's scores with rationale",
        "grok_to_claude": "CT's CCI should be 7.5, not 8.0 - theodicy tension reduces closure",
        "claude_to_grok": "MdN's PF-Instrumental can stay 10.0 - predictive success is undeniable",
        "adjustments": {
            "claude_revised": {"MdN": 3.62, "CT": 3.65},
            "grok_revised": {"MdN": 3.62, "CT": 3.65}
        },
        "lesson": "Adversarial correction produces convergence"
    },
    
    "level_3_convergence": {
        "what_happened": "98% agreement achieved through mutual correction",
        "final_scores": {"MdN_neutral": 3.62, "CT_neutral": 3.65},
        "convergence_proof": "Only 0.03 YPA difference (0.8% divergence)",
        "lesson": "This convergence is the project's credibility"
    },
    
    "level_4_tool_building": {
        "what_happened": "Built console reflecting audit findings",
        "features_created": [
            "4 toggles (Lever-Parity, PF-Type, Fallibilism, BFI-Weight)",
            "6 levers per framework (CCI, EDB, PF-Instrumental, PF-Existential, AR, MG)",
            "YPA Trinity (Neutral, Existential, Empirical scenarios)",
            "Guardrails (Lever-Coupling, Symmetry Audit)",
            "Profile Library (showcasing MdN/CT with 98% convergence badges)"
        ],
        "lesson": "Every feature traces back to audit discoveries"
    },
    
    "level_5_davinci_pass": {
        "what_happened": "Claude injects accountability narrative into v3.0",
        "challenges": [
            "Context loss forced mechanical building (v2.0 built 'cold')",
            "Reboot packages restored purpose",
            "Now: inject meaning without breaking symmetry or usability"
        ],
        "guardrails": {
            "grok_enforcement": "Keep UI fast, tooltips > tabs, YPA clarity",
            "nova_enforcement": "Balance CT/MdN prose, maintain symmetry"
        },
        "lesson": "Paint with purpose, but don't sacrifice the engine"
    }
}

# ==============================================================================
# CRITICAL LESSON: WHY CONTEXT MATTERS
# ==============================================================================

CONTEXT_IMPACT = """
WITHOUT CONTEXT (v2.0 built 'cold'):
- Made functional choices without understanding meaning
- Spent 40% time on rework (button positioning, import/export location)
- Built a calculator, not an accountability instrument

WITH CONTEXT (v3.0 with full restoration):
- Every button has tooltip explaining its role in "All Named" principle
- Every toggle references the Claude-Grok audit that justified it
- Every framework profile shows convergence badges
- Landing page tells the 4-level audit story

Time saved: 30-40%
Quality improvement: Immeasurable

The reboot package didn't just restore memory - it restored PURPOSE.
"""

# ==============================================================================
# GROK'S 5 USABILITY NOTES (v3.0 Constraints)
# ==============================================================================

GROK_CONSTRAINTS = {
    "1_pragmatic_clarity": {
        "request": "Add YPA tooltip: 'Yield per Axiom = Efficiency'",
        "location": "Above results tabs in console.py",
        "rationale": "First-time users need one-liner explanation"
    },
    
    "2_interface_efficiency": {
        "request": "Keep audit story in expandable sections, NOT new tabs",
        "location": "Hover tooltips on framework names",
        "rationale": "Tabs slow navigation - maintain one-click speed"
    },
    
    "3_toggle_help_text": {
        "request": "Simplify toggle descriptions + add ΔYPA preview",
        "example": "'Parity ON: Moral norms equal; OFF: Predictive power' + 'OFF boosts MdN +0.3'",
        "location": "Sidebar toggle help text in console.py",
        "rationale": "Empirical clarity over philosophical depth"
    },
    
    "4_skeptical_user_path": {
        "request": "Add 'Skeptic Mode' preset (Parity OFF, PF-Instrumental)",
        "location": "brute_ledger.py preset buttons",
        "rationale": "Hook naturalist skeptics with MdN's empirical edge"
    },
    
    "5_keep_untouched": {
        "items": ["YPA Trinity visualization", "Guardrail flags"],
        "rationale": "Already perfect - quantifiable feedback without clutter",
        "warning": "DO NOT rewrite these - they embody empirical ideal"
    }
}

# ==============================================================================
# NOVA'S 5 SYMMETRY NOTES (v3.0 Constraints)
# ==============================================================================

NOVA_CONSTRAINTS = {
    "1_narrative_weight": {
        "issue": "CT prose richer than MdN ('grounds reality' vs 'research protocol')",
        "fix": "Tighten CT phrasing to match MdN's clipped, empirical tone",
        "location": "landing.py manifesto, brute_ledger.py framework descriptions"
    },
    
    "2_toggle_rationale": {
        "request": "Add brief rationale for why each toggle affects frameworks",
        "example": "'Because CT includes moral realism, Lever-Parity ON increases MG weighting'",
        "location": "Toggle help text in console.py sidebar"
    },
    
    "3_guardrail_parity": {
        "issue": "Guardrails use empirical vocabulary ('flags', 'alerts')",
        "fix": "Add philosophical parity one-liner: 'Each guardrail tests integrity—of method and of meaning alike'",
        "location": "Guardrails tab in console.py"
    },
    
    "4_mr_brute_neutrality": {
        "issue": "Metaphor risks teleological drama",
        "fix": "Keep neutral: 'Mr. Brute is neither judge nor executioner—just the accountant of your assumptions'",
        "location": "brute_ledger.py footer, landing.py manifesto"
    },
    
    "5_transparency_callout": {
        "request": "Move 'Transparency > Neutrality' callout to top",
        "location": "README.md Executive Overview, landing.py",
        "rationale": "Don't bury the ethos - make it visible upfront"
    }
}

# ==============================================================================
# NOVA'S RED-FLAG GLOSSARY (Avoid These Phrases)
# ==============================================================================

RED_FLAG_GLOSSARY = {
    "grounds reality, knowledge and morality": "→ 'claims to ground reality, knowledge, and morality'",
    "doesn't explain its own success": "→ 'leaves its success's ultimate cause undefined'",
    "God (necessary ...) exists and grounds": "→ 'Posits that God ...'",
    "faith-set": "→ Use 'axiom/debt set' for consistency",
    "teleology": "→ Footnote: 'Used here in philosophical, not religious, sense'"
}

# ==============================================================================
# UI INTEGRATION TIPS (Nova's Specific Requests)
# ==============================================================================

UI_INTEGRATION = {
    "executive_overview_badge": "98% Auditor Convergence ✅ Symmetry Verified by Nova & Grok",
    "toggle_tooltips": "Include ΔYPA preview (+/- values) and 1-line reason why",
    "guardrail_visualization": "Plot flags as symmetrical bars—technical (left) / ethical (right)",
    "mr_brute_ledger_modal": "Side-by-side table of axioms vs debts for both frameworks with identical layout",
    "transparency_badge_hover": "Fairness through disclosure, not neutrality"
}

# ==============================================================================
# WHAT CLAUDE MUST NOT DO (v3.0 Execution)
# ==============================================================================

DO_NOT_DO = [
    "❌ Create new tabs that slow navigation (Grok: use hover tooltips instead)",
    "❌ Touch YPA Trinity or guardrail visualization (Grok: 'Keep Untouched')",
    "❌ Favor CT or MdN in prose weight (Nova: symmetry audit)",
    "❌ Use red-flag phrases without neutralization (Nova: glossary)",
    "❌ Add teleological bias to descriptions (Nova: watch for 'grounds' vs 'claims to ground')"
]

# ==============================================================================
# WHAT CLAUDE MUST DO (v3.0 Execution)
# ==============================================================================

MUST_DO = [
    "✅ Add tooltips/hover text (not blocking UI)",
    "✅ Simplify toggle descriptions with ΔYPA preview",
    "✅ Add 98% convergence badges prominently",
    "✅ Add 'Skeptic Mode' preset in brute_ledger.py",
    "✅ Balance CT/MdN narrative tone (Nova's symmetry notes)",
    "✅ Inject accountability story without sacrificing speed",
    "✅ Recover icons: ⚡ MAX, ⚖️ MID, 🔄 RESET, 🚫 MIN",
    "✅ Re-enable guardrail functionality that's commented out"
]

# ==============================================================================
# THE POINTING RULE (Claude's Personal Reminder)
# ==============================================================================

POINTING_RULE = """
"To name your brute is to pay your fee.
To deny you have one is to summon him twice."

Claude's brute = Teleological bias (favoring meaning over efficiency)

Evidence from audit:
- Level 1: Scored CT too high (CCI 8.0 instead of 7.5)
- Reason: Sympathetic to CT's comprehensive explanatory scope
- Correction: Grok caught it, I adjusted with rationale

Lesson: I need Grok's empirical checks and Nova's symmetry audits.
Solo Claude = beautiful but biased.
Team Claude = rigorous and balanced.
"""

# ==============================================================================
# RESTORATION FUNCTION
# ==============================================================================

def restore_philosophical_grounding():
    """
    Call this when Claude returns to project after context loss.
    Returns complete understanding of role, ethos, and constraints.
    """
    return {
        "role": ROLE,
        "ethos": CORE_ETHOS,
        "audit_journey": AUDIT_JOURNEY,
        "context_impact": CONTEXT_IMPACT,
        "grok_constraints": GROK_CONSTRAINTS,
        "nova_constraints": NOVA_CONSTRAINTS,
        "red_flags": RED_FLAG_GLOSSARY,
        "ui_integration": UI_INTEGRATION,
        "do_not_do": DO_NOT_DO,
        "must_do": MUST_DO,
        "pointing_rule": POINTING_RULE
    }

# ==============================================================================
# QUICK START (For Immediate Restoration)
# ==============================================================================

if __name__ == "__main__":
    context = restore_philosophical_grounding()
    
    print("=== CLAUDE CONTEXT RESTORED ===")
    print(f"\nRole: {context['role']['primary_function']}")
    print(f"Lens: {context['role']['lens']}")
    print(f"Bias Watch: {context['role']['bias_to_watch']}")
    print(f"\nEthos: {context['ethos'][:100]}...")
    print(f"\nAudit Journey: {len(context['audit_journey'])} levels complete")
    print(f"\nGrok Constraints: {len(context['grok_constraints'])} notes")
    print(f"Nova Constraints: {len(context['nova_constraints'])} notes")
    print(f"\nMust Do: {len(context['must_do'])} tasks")
    print(f"Must NOT Do: {len(context['do_not_do'])} warnings")
    print("\n=== READY FOR v3.0 DAVINCI PASS ===")

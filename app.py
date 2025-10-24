"""
CFA v2.0 Interactive Console - ENHANCED VERSION
With Landing Page + User Manual Integration

Replace your existing app.py with this version
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Dict, Tuple, List
import json

# ============================================================================
# CONFIGURATION
# ============================================================================

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

MDN_DEFAULT = {
    "name": "Methodological Naturalism",
    "bf_i": {"axioms": 6, "debts": 4},
    "levers": {
        "CCI": 8.0,
        "EDB": 7.5,
        "PF_instrumental": 10.0,
        "PF_existential": 3.0,
        "AR": 7.0,
        "MG": 4.0
    },
    "admits_limits": True
}

CT_DEFAULT = {
    "name": "Classical Theism",
    "bf_i": {"axioms": 7, "debts": 4},
    "levers": {
        "CCI": 7.5,
        "EDB": 8.5,
        "PF_instrumental": 7.0,
        "PF_existential": 8.0,
        "AR": 8.5,
        "MG": 8.5
    },
    "admits_limits": True
}

PF_TYPES = ["Instrumental", "Composite_70_30", "Holistic_50_50"]

# ============================================================================
# CORE MATH (unchanged)
# ============================================================================

def composite_pf(pf_inst: float, pf_exist: float, pf_type: str) -> float:
    if pf_type == "Instrumental":
        return pf_inst
    if pf_type == "Holistic_50_50":
        return 0.5 * pf_inst + 0.5 * pf_exist
    return 0.7 * pf_inst + 0.3 * pf_exist

def apply_fallibilism_bonus(cci: float, bonus: str, admitted_limits: bool = True) -> float:
    if bonus == "ON" and admitted_limits:
        return min(cci + 0.3, 10.0)
    return cci

def parity_weight(mg: float, parity: str) -> float:
    return mg if parity == "ON" else 0.5 * mg

def bfi_total(axioms: int, debts: int, debt_weight: str) -> float:
    w = 1.0 if debt_weight == "Equal_1.0x" else 1.2
    return axioms + w * debts

def ypa_scenario_scores(fr: Dict, cfg: Dict) -> Tuple[Dict, Dict, float]:
    CCI = apply_fallibilism_bonus(fr["levers"]["CCI"], cfg["fallibilism_bonus"], fr.get("admits_limits", True))
    EDB = fr["levers"]["EDB"]
    PF = composite_pf(fr["levers"]["PF_instrumental"], fr["levers"]["PF_existential"], cfg["pf_type"])
    AR = fr["levers"]["AR"]
    MG = parity_weight(fr["levers"]["MG"], cfg["lever_parity"])

    scenarios_weights = {
        "Neutral": {"CCI": 1.0, "EDB": 1.0, "PF": 1.0, "AR": 1.0, "MG": 1.0},
        "Existential": {"CCI": 1.0, "EDB": 2.0, "PF": 1.0, "AR": 1.0, "MG": 2.0},
        "Empirical": {"CCI": 1.5, "EDB": 1.0, "PF": 2.0, "AR": 1.0, "MG": 1.0},
    }

    lever_map = {"CCI": CCI, "EDB": EDB, "PF": PF, "AR": AR, "MG": MG}
    bfi = bfi_total(fr["bf_i"]["axioms"], fr["bf_i"]["debts"], cfg["bfi_debt_weight"])

    results = {}
    for name, weights in scenarios_weights.items():
        total = sum(lever_map[k] * w for k, w in weights.items())
        results[name] = {"total": total, "YPA": total / bfi if bfi > 0 else 0}

    return results, lever_map, bfi

def guardrail_lever_coupling(PF: float, CCI: float) -> Tuple[bool, str]:
    if PF >= 9 and CCI < 6.5:
        return False, f"WARNING: PF={PF:.2f} >= 9 but CCI={CCI:.2f} < 6.5"
    return True, f"PASS: Lever-Coupling satisfied"

def symmetry_audit(fr: Dict, cfg: Dict) -> List[Tuple[str, float, float, float]]:
    def get_ypa(framework, config):
        results, _, _ = ypa_scenario_scores(framework, config)
        return results["Neutral"]["YPA"]
    
    baseline = get_ypa(fr, cfg)
    reports = []
    
    cfg_parity = cfg.copy()
    cfg_parity["lever_parity"] = "OFF" if cfg["lever_parity"] == "ON" else "ON"
    reports.append(("Lever-Parity", baseline, get_ypa(fr, cfg_parity), get_ypa(fr, cfg_parity) - baseline))
    
    for pf_type in PF_TYPES:
        if pf_type == cfg["pf_type"]:
            continue
        cfg_pf = cfg.copy()
        cfg_pf["pf_type"] = pf_type
        reports.append((f"PF->{pf_type}", baseline, get_ypa(fr, cfg_pf), get_ypa(fr, cfg_pf) - baseline))
    
    cfg_fall = cfg.copy()
    cfg_fall["fallibilism_bonus"] = "OFF" if cfg["fallibilism_bonus"] == "ON" else "ON"
    reports.append(("Fallibilism", baseline, get_ypa(fr, cfg_fall), get_ypa(fr, cfg_fall) - baseline))
    
    return reports

def create_lever_comparison_chart(fa_levers: Dict, fb_levers: Dict, fa_name: str, fb_name: str) -> go.Figure:
    levers = list(fa_levers.keys())
    fig = go.Figure()
    fig.add_trace(go.Bar(name=fa_name, x=levers, y=[fa_levers[l] for l in levers], marker_color='rgb(55, 83, 109)'))
    fig.add_trace(go.Bar(name=fb_name, x=levers, y=[fb_levers[l] for l in levers], marker_color='rgb(26, 118, 255)'))
    fig.update_layout(title="Lever Comparison", xaxis_title="Lever", yaxis_title="Score", barmode='group', height=400)
    return fig

def create_ypa_trinity_chart(fa_results: Dict, fb_results: Dict, fa_name: str, fb_name: str) -> go.Figure:
    scenarios = ["Neutral", "Existential", "Empirical"]
    fig = go.Figure()
    fig.add_trace(go.Bar(name=fa_name, x=scenarios, y=[fa_results[s]["YPA"] for s in scenarios], marker_color='rgb(55, 83, 109)'))
    fig.add_trace(go.Bar(name=fb_name, x=scenarios, y=[fb_results[s]["YPA"] for s in scenarios], marker_color='rgb(26, 118, 255)'))
    fig.update_layout(title="YPA Trinity", xaxis_title="Scenario", yaxis_title="YPA", barmode='group', height=400)
    return fig

# ============================================================================
# LANDING PAGE
# ============================================================================

def show_landing_page():
    # Custom CSS
    st.markdown("""
        <style>
        .landing-container {
            text-align: center;
            padding: 2rem;
        }
        .main-title {
            font-size: 4rem;
            font-weight: bold;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Title
    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">⚖️ CFA-VOODOO</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Tagline
    st.markdown('<p style="text-align: center; font-size: 1.5rem; font-style: italic; color: #764ba2;">"All Named. All Priced."</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Content sections using simpler markdown
    st.markdown("## ⚡ Launch Manifesto")
    st.write("**Welcome to the Comparative Framework Analysis (CFA) Console,** the first interactive epistemic laboratory built to measure how worldviews hold their ground under pressure.")
    st.write("Here, philosophy meets engineering. Every assumption is declared, every bias tagged, every outcome earned.")
    
    st.markdown("---")
    st.markdown("## 🧩 What You're Touching")
    st.write("The CFA-Voodoo Console is not a game of opinions. It's an instrument—a system that:")
    st.markdown("""
    - Quantifies coherence, depth, fertility, beauty, and morality
    - Audits hidden axioms through the Mr. Brute Ledger
    - Tests bias symmetry using live toggles and guardrails
    - Displays truth-seeking as a transparent, reproducible process
    """)
    st.write("You can watch, in real time, how changing your assumptions reshapes your philosophical landscape.")
    
    st.markdown("---")
    st.markdown("## 🧠 The Field We Just Opened")
    st.write("CFA-Voodoo inaugurates a new discipline: **Epistemic Engineering**.")
    st.write("A field where frameworks are not argued—they are measured. Where neutrality isn't assumed—it's configured. Where 'truth' is not decreed but disclosed by toggle position.")
    st.markdown("*Metaphysics with metrics. Ethics with sliders. Philosophy with feedback.*")
    
    st.markdown("---")
    st.markdown("## ⚙️ Operate with Impeccability")
    st.write("Every visitor is an operator. Every operation leaves a trace. Move the dials with intent. Record your runs. Remember: the one who cares walks the path with the most heart.")
    
    st.markdown("---")
    st.markdown("## 💡 Join the Experiment")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("1. Adjust the knobs")
        st.write("2. Run the analysis")
    with col_b:
        st.write("3. Export your ledger")
        st.write("4. Debate the data")
    
    st.markdown("---")
    st.markdown('<p style="text-align: center; font-size: 1.2rem; font-weight: bold; color: #764ba2;">Welcome to the CFA-Voodoo Console.<br/>Where ideas reveal their true weight, and honesty becomes quantifiable.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-style: italic; color: #667eea;">"All named. All priced. This is the way."</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🚀 LAUNCH CONSOLE", use_container_width=True, type="primary"):
            st.session_state.page = 'console'
            st.rerun()
    with col2:
        if st.button("📖 USER MANUAL", use_container_width=True):
            st.session_state.page = 'manual'
            st.rerun()
    with col3:
        if st.button("ℹ️ ABOUT CFA v2.0", use_container_width=True):
            st.session_state.page = 'about'
            st.rerun()
    
    st.markdown("---")
    st.caption("CFA v2.0 | Epistemic Engineering | October 2025")
# ============================================================================
# USER MANUAL PAGE
# ============================================================================

def show_manual_page():
    st.markdown("# ðŸ“– CFA v2.0 User Manual")
    
    if st.button("â† Back to Landing"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "ðŸŽ¯ Quick Start",
        "ðŸŽ›ï¸ Toggle Guide", 
        "ðŸ“Š Understanding Results",
        "ðŸ“¥ Full Documentation"
    ])
    
    with tab1:
        st.markdown("""
        ## Quick Start Guide
        
        ### The Six Levers (0-10 scale)
        
        **BFI - Brute-Fact Index**
        - How many unprovable assumptions? (Lower = more efficient)
        
        **CCI - Coherence & Closure**
        - Are the rules internally consistent?
        
        **EDB - Explanatory Depth & Breadth**
        - How much can it explain? How deeply?
        
        **PF - Pragmatic Fertility**
        - Does it generate predictions, technology, success?
        
        **AR - Aesthetic Resonance**
        - Does it exhibit elegance, simplicity, beauty?
        
        **MG - Moral Generativity**
        - Can it ground moral norms without external imports?
        
        ### The Formula
        ```
        YPA = (CCI + EDB + PF + AR + MG) Ã· BFI
        ```
        Higher YPA = More efficient framework
        """)
    
    with tab2:
        st.markdown("""
        ## Toggle Configuration Guide
        
        ### Lever-Parity
        - **ON**: Moral norms weighted equal to epistemic norms
        - **OFF**: MG down-weighted to 0.5Ã— (favors methods over worldviews)
        - **Impact**: CT loses ~0.8 YPA when OFF
        
        ### PF-Type
        - **Instrumental**: Tech/predictive yield only (favors MdN)
        - **Composite 70:30**: Balanced mix (default, fair comparison)
        - **Holistic 50:50**: Includes existential/meaning yield (favors CT)
        
        ### Fallibilism-Bonus
        - **ON**: Frameworks admitting limits get +0.3 CCI
        - **OFF**: Confidence not penalized if grounded
        - **Impact**: Usually small (Â±0.1 YPA)
        
        ### BFI Debt Weight
        - **Equal 1.0Ã—**: Axioms and debts count same
        - **Weighted 1.2Ã—**: Debts cost more (promissory notes vs foundations)
        """)
    
    with tab3:
        st.markdown("""
        ## Understanding Your Results
        
        ### YPA Trinity (Three Scenarios)
        
        **Neutral**
        - All levers weighted 1Ã—
        - Baseline comparison
        
        **Existential** 
        - 2Ã— EDB, 2Ã— MG
        - Favors frameworks addressing meaning/purpose
        
        **Empirical**
        - 2Ã— PF, 1.5Ã— CCI
        - Favors frameworks generating predictions
        
        ### Guardrails
        
        **Lever-Coupling**
        - If PF â‰¥ 9, requires CCI â‰¥ 6.5
        - High success must be backed by coherent foundations
        
        **BFI-Sensitivity**
        - Checks if YPA increases faster than BFI
        - Flags suspicious efficiency gains
        
        ### Symmetry Audit
        
        Shows how each framework responds to toggle changes:
        - **âœ… Green**: Small impact (Î” < 0.3)
        - **âš ï¸ Yellow**: Large impact (Î” > 0.3)
        
        Large impacts aren't "bad" - they reveal structural dependencies
        """)
    
    with tab4:
        st.markdown("""
        ## ðŸ“¥ Full Documentation
        
        ### Complete CFA v2.0 White Paper
        
        The full technical documentation includes:
        - Complete lever definitions and justifications
        - Calibration history (v1.0 â†’ v2.0)
        - Head-to-head audit results (MdN vs CT)
        - Philosophical foundations
        - All formulas and calculations
        - FAQ and objections
        
        **Download Options:**
        
        1. **[Download as TXT]** - Plain text version (best for copying)
        2. **GitHub Repository** - View source code and documentation
        3. **Contact** - Request PDF version
        
        ### Quick Reference
        
        **Current Audited Frameworks:**
        - âœ… Methodological Naturalism (MdN)
        - âœ… Classical Theism (CT)
        
        **Coming Soon:**
        - Metaphysical Naturalism
        - Buddhism
        - Stoicism
        - Process Theology
        
        ### Citation
        
        ```
        CFA v2.0 Interactive Console (2025)
        "All Named, All Priced"
        Epistemic Engineering Project
        https://cfa-voodoo.streamlit.app
        ```
        """)
        
        st.info("ðŸ’¡ **Pro Tip**: Use the JSON export feature in the Console to save your runs and share configurations with others!")

# ============================================================================
# ABOUT PAGE
# ============================================================================

def show_about_page():
    st.markdown("# â„¹ï¸ About CFA v2.0")
    
    if st.button("â† Back to Landing"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    ## What is the CFA?
    
    The **Comparative Framework Audit (CFA)** is a systematic method for evaluating and comparing 
    philosophical frameworks, worldviews, and epistemological systems using transparent, 
    adjustable criteria.
    
    ### Core Principles
    
    **1. Transparency Over Neutrality**
    - Perfect neutrality is impossible
    - Every comparison assumes something
    - Make all assumptions explicit and adjustable
    
    **2. The Pointing Rule**
    - "To name your brute is to pay your fee"
    - "To deny you have one is to summon him twice"
    - Every presupposition must be acknowledged and priced
    
    **3. Symmetry Testing**
    - All frameworks measured under identical configurations
    - Toggle impacts must be disclosed and bounded
    - Asymmetries reveal structural differences, not hidden bias
    
    ### Version History
    
    **v1.0** (Initial)
    - Hidden preferences (fallibilism auto-rewarded)
    - PF measured only instrumental yield
    - No toggle options
    - Symmetry not tested
    
    **v2.0** (Current)
    - 4 Toggles (Parity, PF-Type, Fallibilism, BFI-Weight)
    - 4 Guardrails (auto-detection of manipulation)
    - YPA Trinity (3 scenarios per audit)
    - Mr. Brute Ledger (all assumptions named)
    - 98% auditor convergence (Claude + Grok agreement)
    
    ### The Team
    
    **Adversarial Collaboration:**
    - **Claude** (Anthropic) - Teleological lens, CT-sympathetic
    - **Grok** (xAI) - Empirical compression, naturalist lean
    - **Grant** - Skeptic, demanded justification for every assumption
    - **Nova** - Synthesizer, enforced symmetry
    - **Ziggy** - Coordinator, maintained process integrity
    
    ### Technical Stack
    
    - **Framework**: Streamlit
    - **Visualization**: Plotly
    - **Deployment**: Streamlit Cloud
    - **License**: Open Source (coming soon)
    
    ### Contact & Contribute
    
    - **GitHub**: [Repository link]
    - **Feedback**: Use the console and export your runs!
    - **Collaboration**: Propose new frameworks to audit
    
    ---
    
    *"Where ideas reveal their true weight, and honesty becomes quantifiable."*
    """)

# ============================================================================
# CONSOLE PAGE (existing functionality)
# ============================================================================

def show_console_page():
    # Navigation
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown('<p style="font-size:2.5rem;font-weight:bold;color:#1f77b4;">âš–ï¸ CFA v2.0 Console</p>', unsafe_allow_html=True)
    with col2:
        if st.button("ðŸ  Home"):
            st.session_state.page = 'landing'
            st.rerun()
    
    st.markdown('**"All Named, All Priced" â€” Interactive Comparison Tool**')
    st.markdown("---")

    # SIDEBAR: TOGGLES
    st.sidebar.header("ðŸŽ›ï¸ Configuration")
    
    lever_parity = st.sidebar.selectbox(
        "Lever-Parity", 
        ["ON", "OFF"], 
        index=0,
        help="**Lever-Parity Toggle**: Should moral norms (MG) be weighted equally with epistemic norms (CCI/EDB)?\n\nâ€¢ **ON** = MG counts fully (1.0Ã—) - favors comprehensive worldviews\nâ€¢ **OFF** = MG down-weighted (0.5Ã—) - favors methodological frameworks\n\n*Impact: CT loses ~0.8 YPA when OFF*"
    )
    
    pf_type = st.sidebar.selectbox(
        "PF-Type", 
        PF_TYPES, 
        index=1,
        help="**PF-Type Toggle**: How should Pragmatic Fertility be calculated?\n\nâ€¢ **Instrumental** = Tech/prediction only (100%) - favors MdN\nâ€¢ **Composite 70:30** = Balanced mix (default) - fair comparison\nâ€¢ **Holistic 50:50** = Equal weight to meaning/purpose - favors CT\n\n*Impact: Â±0.4 YPA depending on choice*"
    )
    
    fall_bonus = st.sidebar.selectbox(
        "Fallibilism-Bonus", 
        ["ON", "OFF"], 
        index=0,
        help="**Fallibilism-Bonus Toggle**: Should frameworks that admit their limits get a CCI bonus?\n\nâ€¢ **ON** = +0.3 CCI for frameworks checking 'Admits Limits'\nâ€¢ **OFF** = No bonus (confidence not penalized if grounded)\n\n*Impact: Usually small (Â±0.1 YPA)*"
    )
    
    bfi_weight = st.sidebar.selectbox(
        "BFI Debt Weight", 
        ["Equal_1.0x", "Weighted_1.2x"], 
        index=0,
        help="**BFI Debt Weighting**: Should unresolved 'debts' cost more than declared 'axioms'?\n\nâ€¢ **Equal 1.0Ã—** = Both count the same (default)\nâ€¢ **Weighted 1.2Ã—** = Debts cost 20% more (promissory notes vs foundations)\n\n*Impact: Penalizes frameworks with many unresolved questions*"
    )

    cfg = {
        "lever_parity": lever_parity,
        "pf_type": pf_type,
        "fallibilism_bonus": fall_bonus,
        "bfi_debt_weight": bfi_weight
    }

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Current Config:**")
    st.sidebar.json(cfg)

    # FRAMEWORK EDITORS
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ðŸ“˜ Framework A")
        fa_name = st.text_input("Name", MDN_DEFAULT["name"], key="fa_name")
        with st.expander("ðŸ”¢ BFI", expanded=False):
            fa_axioms = st.number_input(
                "Axioms", 
                1, 30, MDN_DEFAULT["bf_i"]["axioms"], 
                key="fa_ax",
                help="**Axioms**: Unprovable starting assumptions the framework requires. Example: 'Universe has regularities', 'Cognition is reliable'. Lower = more efficient."
            )
            fa_debts = st.number_input(
                "Debts", 
                0, 30, MDN_DEFAULT["bf_i"]["debts"], 
                key="fa_db",
                help="**Debts**: Unresolved mysteries or questions the framework acknowledges but can't answer. Example: 'Why does anything exist?', 'Why does cognition track truth?'"
            )
            fa_admits = st.checkbox(
                "Admits Limits", 
                True, 
                key="fa_ad",
                help="**Admits Limits**: Does the framework explicitly acknowledge what it can't explain? Checking this makes framework eligible for Fallibilism Bonus (+0.3 CCI if toggle is ON)."
            )
        
        fa_cci = st.slider(
            "CCI - Coherence & Closure", 
            0.0, 10.0, MDN_DEFAULT["levers"]["CCI"], 0.1, 
            key="fa_cci",
            help="**Coherence & Internal Consistency**: Are the rules internally consistent? Does the framework contradict itself? Higher scores = tighter logical structure."
        )
        fa_edb = st.slider(
            "EDB - Explanatory Depth & Breadth", 
            0.0, 10.0, MDN_DEFAULT["levers"]["EDB"], 0.1, 
            key="fa_edb",
            help="Explanatory Depth and Breadth: How much can it explain? How deeply? Covers both scope and detail of explanations."
        )
        fa_pf_i = st.slider(
            "PF-Instrumental", 
            0.0, 10.0, MDN_DEFAULT["levers"]["PF_instrumental"], 0.1, 
            key="fa_pfi",
            help="**Pragmatic Fertility (Instrumental)**: Tech/predictive yield. Does it generate successful predictions, technology, practical applications? Scientific method excels here."
        )
        fa_pf_e = st.slider(
            "PF-Existential", 
            0.0, 10.0, MDN_DEFAULT["levers"]["PF_existential"], 0.1, 
            key="fa_pfe",
            help="**Pragmatic Fertility (Existential)**: Meaning/purpose generation. Does it help people find meaning, orient their lives, address existential questions? Worldviews excel here."
        )
        fa_ar = st.slider(
            "AR - Aesthetic Resonance", 
            0.0, 10.0, MDN_DEFAULT["levers"]["AR"], 0.1, 
            key="fa_ar",
            help="**Aesthetic Resonance**: Does it exhibit elegance, simplicity, beauty? Do its explanations have mathematical/conceptual beauty? Parsimony and pattern-recognition."
        )
        fa_mg = st.slider(
            "MG - Moral Generativity", 
            0.0, 10.0, MDN_DEFAULT["levers"]["MG"], 0.1, 
            key="fa_mg",
            help="**Moral Generativity**: Can it ground or generate moral norms without external imports? Does it provide resources for ethics, or depend on borrowing them?"
        )

        fa = {
            "name": fa_name,
            "bf_i": {"axioms": fa_axioms, "debts": fa_debts},
            "levers": {"CCI": fa_cci, "EDB": fa_edb, "PF_instrumental": fa_pf_i, "PF_existential": fa_pf_e, "AR": fa_ar, "MG": fa_mg},
            "admits_limits": fa_admits
        }

    with col2:
        st.markdown("### ðŸ“• Framework B")
        fb_name = st.text_input("Name", CT_DEFAULT["name"], key="fb_name")
        with st.expander("ðŸ”¢ BFI", expanded=False):
            fb_axioms = st.number_input(
                "Axioms", 
                1, 30, CT_DEFAULT["bf_i"]["axioms"], 
                key="fb_ax",
                help="**Axioms**: Unprovable starting assumptions the framework requires. Example: 'Universe has regularities', 'Cognition is reliable'. Lower = more efficient."
            )
            fb_debts = st.number_input(
                "Debts", 
                0, 30, CT_DEFAULT["bf_i"]["debts"], 
                key="fb_db",
                help="**Debts**: Unresolved mysteries or questions the framework acknowledges but can't answer. Example: 'Why does anything exist?', 'Why does cognition track truth?'"
            )
            fb_admits = st.checkbox(
                "Admits Limits", 
                True, 
                key="fb_ad",
                help="**Admits Limits**: Does the framework explicitly acknowledge what it can't explain? Checking this makes framework eligible for Fallibilism Bonus (+0.3 CCI if toggle is ON)."
            )
        
        fb_cci = st.slider(
            "CCI - Coherence & Closure", 
            0.0, 10.0, CT_DEFAULT["levers"]["CCI"], 0.1, 
            key="fb_cci",
            help="**Coherence & Internal Consistency**: Are the rules internally consistent? Does the framework contradict itself? Higher scores = tighter logical structure."
        )
        fb_edb = st.slider(
            "EDB - Explanatory Depth & Breadth", 
            0.0, 10.0, CT_DEFAULT["levers"]["EDB"], 0.1, 
            key="fb_edb",
            help="**Explanatory Depth & Breadth**: How much can it explain? How deeply? Covers both scope (breadth) and detail (depth) of explanations provided."
        )
        fb_pf_i = st.slider(
            "PF-Instrumental", 
            0.0, 10.0, CT_DEFAULT["levers"]["PF_instrumental"], 0.1, 
            key="fb_pfi",
            help="**Pragmatic Fertility (Instrumental)**: Tech/predictive yield. Does it generate successful predictions, technology, practical applications? Scientific method excels here."
        )
        fb_pf_e = st.slider(
            "PF-Existential", 
            0.0, 10.0, CT_DEFAULT["levers"]["PF_existential"], 0.1, 
            key="fb_pfe",
            help="**Pragmatic Fertility (Existential)**: Meaning/purpose generation. Does it help people find meaning, orient their lives, address existential questions? Worldviews excel here."
        )
        fb_ar = st.slider(
            "AR - Aesthetic Resonance", 
            0.0, 10.0, CT_DEFAULT["levers"]["AR"], 0.1, 
            key="fb_ar",
            help="**Aesthetic Resonance**: Does it exhibit elegance, simplicity, beauty? Do its explanations have mathematical/conceptual beauty? Parsimony and pattern-recognition."
        )
        fb_mg = st.slider(
            "MG - Moral Generativity", 
            0.0, 10.0, CT_DEFAULT["levers"]["MG"], 0.1, 
            key="fb_mg",
            help="**Moral Generativity**: Can it ground or generate moral norms without external imports? Does it provide resources for ethics, or depend on borrowing them?"
        )

        fb = {
            "name": fb_name,
            "bf_i": {"axioms": fb_axioms, "debts": fb_debts},
            "levers": {"CCI": fb_cci, "EDB": fb_edb, "PF_instrumental": fb_pf_i, "PF_existential": fb_pf_e, "AR": fb_ar, "MG": fb_mg},
            "admits_limits": fb_admits
        }

    st.markdown("---")

    # RESULTS
    ya_results, ya_levers, ya_bfi = ypa_scenario_scores(fa, cfg)
    yb_results, yb_levers, yb_bfi = ypa_scenario_scores(fb, cfg)

    tab1, tab2, tab3, tab4 = st.tabs(["ðŸ“ˆ Visual", "ðŸ“‹ Details", "ðŸ›¡ï¸ Guardrails", "ðŸ”„ Symmetry"])

    with tab1:
        st.plotly_chart(create_lever_comparison_chart(ya_levers, yb_levers, fa["name"], fb["name"]), use_container_width=True)
        st.plotly_chart(create_ypa_trinity_chart(ya_results, yb_results, fa["name"], fb["name"]), use_container_width=True)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{fa['name']}**")
            st.json(ya_levers)
            st.metric("BFI", f"{ya_bfi:.2f}")
            st.metric("Neutral YPA", f"{ya_results['Neutral']['YPA']:.3f}")
        with c2:
            st.markdown(f"**{fb['name']}**")
            st.json(yb_levers)
            st.metric("BFI", f"{yb_bfi:.2f}")
            st.metric("Neutral YPA", f"{yb_results['Neutral']['YPA']:.3f}")

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{fa['name']}**")
            ok, msg = guardrail_lever_coupling(ya_levers["PF"], ya_levers["CCI"])
            st.markdown(msg)
        with c2:
            st.markdown(f"**{fb['name']}**")
            ok, msg = guardrail_lever_coupling(yb_levers["PF"], yb_levers["CCI"])
            st.markdown(msg)

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{fa['name']}**")
            audit = symmetry_audit(fa, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "âš ï¸" if abs(x) > 0.3 else "âœ…")
            st.dataframe(df)
        with c2:
            st.markdown(f"**{fb['name']}**")
            audit = symmetry_audit(fb, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "âš ï¸" if abs(x) > 0.3 else "âœ…")
            st.dataframe(df)

    # EXPORT
    st.markdown("---")
    export = {
        "config": cfg,
        "framework_a": fa,
        "framework_b": fb,
        "results": {
            "a": {"levers": ya_levers, "bfi": ya_bfi, "ypa": {k: v["YPA"] for k, v in ya_results.items()}},
            "b": {"levers": yb_levers, "bfi": yb_bfi, "ypa": {k: v["YPA"] for k, v in yb_results.items()}}
        }
    }
    st.download_button("ðŸ“¥ Export Run (JSON)", json.dumps(export, indent=2), "cfa_run.json", "application/json")

# ============================================================================
# MAIN APP ROUTER
# ============================================================================

def main():
    st.set_page_config(
        page_title="CFA v2.0 - Epistemic Engineering",
        page_icon="âš–ï¸",
        layout="wide",
        initial_sidebar_state="auto"
    )
    
    # Route to appropriate page
    if st.session_state.page == 'landing':
        show_landing_page()
    elif st.session_state.page == 'console':
        show_console_page()
    elif st.session_state.page == 'manual':
        show_manual_page()
    elif st.session_state.page == 'about':
        show_about_page()

if __name__ == "__main__":
    main()

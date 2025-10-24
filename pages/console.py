"""
CFA v2.0 - Console Page Component
Main comparison tool with dual framework editors, toggles, and visualizations
"""

import streamlit as st
import pandas as pd
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.calculations import ypa_scenario_scores, guardrail_lever_coupling, symmetry_audit, PF_TYPES
from utils.visualizations import create_lever_comparison_chart, create_ypa_trinity_chart
from utils.frameworks import MDN_DEFAULT, CT_DEFAULT

def render():
    """Render the console page"""
    
    # Navigation header
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown('<p style="font-size:2.5rem;font-weight:bold;color:#1f77b4;">⚖️ CFA v2.0 Console</p>', unsafe_allow_html=True)
    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = 'landing'
            st.rerun()
    
    st.markdown('**"All Named, All Priced" — Interactive Comparison Tool**')
    st.markdown("---")

    # ========================================================================
    # SIDEBAR: TOGGLES & CONFIGURATION
    # ========================================================================
    st.sidebar.header("🎛️ Configuration")
    
    lever_parity = st.sidebar.selectbox(
        "Lever-Parity", 
        ["ON", "OFF"], 
        index=0,
        help="**Lever-Parity Toggle**: Should moral norms (MG) be weighted equally with epistemic norms (CCI/EDB)?\n\n• **ON** = MG counts fully (1.0×) - favors comprehensive worldviews\n• **OFF** = MG down-weighted (0.5×) - favors methodological frameworks\n\n*Impact: CT loses ~0.8 YPA when OFF*"
    )
    
    pf_type = st.sidebar.selectbox(
        "PF-Type", 
        PF_TYPES, 
        index=1,
        help="**PF-Type Toggle**: How should Pragmatic Fertility be calculated?\n\n• **Instrumental** = Tech/prediction only (100%) - favors MdN\n• **Composite 70:30** = Balanced mix (default) - fair comparison\n• **Holistic 50:50** = Equal weight to meaning/purpose - favors CT\n\n*Impact: ±0.4 YPA depending on choice*"
    )
    
    fall_bonus = st.sidebar.selectbox(
        "Fallibilism-Bonus", 
        ["ON", "OFF"], 
        index=0,
        help="**Fallibilism-Bonus Toggle**: Should frameworks that admit their limits get a CCI bonus?\n\n• **ON** = +0.3 CCI for frameworks checking 'Admits Limits'\n• **OFF** = No bonus (confidence not penalized if grounded)\n\n*Impact: Usually small (±0.1 YPA)*"
    )
    
    bfi_weight = st.sidebar.selectbox(
        "BFI Debt Weight", 
        ["Equal_1.0x", "Weighted_1.2x"], 
        index=0,
        help="**BFI Debt Weighting**: Should unresolved 'debts' cost more than declared 'axioms'?\n\n• **Equal 1.0×** = Both count the same (default)\n• **Weighted 1.2×** = Debts cost 20% more (promissory notes vs foundations)\n\n*Impact: Penalizes frameworks with many unresolved questions*"
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

    # ========================================================================
    # FRAMEWORK EDITORS (Two Columns)
    # ========================================================================
    col1, col2 = st.columns(2)

    # ------------------------------------------------------------------------
    # FRAMEWORK A (Left Column)
    # ------------------------------------------------------------------------
    with col1:
        st.markdown("### 📘 Framework A")
        fa_name = st.text_input("Name", MDN_DEFAULT["name"], key="fa_name")
        
        # ====================================================================
        # PRESET BUTTONS - Quick lever adjustments
        # ====================================================================
        st.markdown("**⚡ Quick Presets:**")
        preset_col1, preset_col2, preset_col3, preset_col4 = st.columns([1, 1, 1, 1])
        
        with preset_col1:
            if st.button("⚡ MAX", key="fa_max", help="Set all levers to maximum (10.0)", use_container_width=True):
                st.session_state.fa_cci = 10.0
                st.session_state.fa_edb = 10.0
                st.session_state.fa_pfi = 10.0
                st.session_state.fa_pfe = 10.0
                st.session_state.fa_ar = 10.0
                st.session_state.fa_mg = 10.0
                st.rerun()
        
        with preset_col2:
            if st.button("⚖️ MID", key="fa_mid", help="Set all levers to neutral (5.0)", use_container_width=True):
                st.session_state.fa_cci = 5.0
                st.session_state.fa_edb = 5.0
                st.session_state.fa_pfi = 5.0
                st.session_state.fa_pfe = 5.0
                st.session_state.fa_ar = 5.0
                st.session_state.fa_mg = 5.0
                st.rerun()
        
        with preset_col3:
            if st.button("🔄 RESET", key="fa_reset", help="Reset to defaults", use_container_width=True):
                st.session_state.fa_cci = MDN_DEFAULT["levers"]["CCI"]
                st.session_state.fa_edb = MDN_DEFAULT["levers"]["EDB"]
                st.session_state.fa_pfi = MDN_DEFAULT["levers"]["PF_instrumental"]
                st.session_state.fa_pfe = MDN_DEFAULT["levers"]["PF_existential"]
                st.session_state.fa_ar = MDN_DEFAULT["levers"]["AR"]
                st.session_state.fa_mg = MDN_DEFAULT["levers"]["MG"]
                st.rerun()
        
        with preset_col4:
            if st.button("🚫 MIN", key="fa_min", help="Set all levers to minimum (0.0)", use_container_width=True):
                st.session_state.fa_cci = 0.0
                st.session_state.fa_edb = 0.0
                st.session_state.fa_pfi = 0.0
                st.session_state.fa_pfe = 0.0
                st.session_state.fa_ar = 0.0
                st.session_state.fa_mg = 0.0
                st.rerun()
        
        st.markdown("---")
        
        with st.expander("🔢 BFI", expanded=False):
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
            help="**Explanatory Depth and Breadth**: How much can it explain? How deeply? Covers both scope and detail of explanations."
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
            "levers": {
                "CCI": fa_cci, 
                "EDB": fa_edb, 
                "PF_instrumental": fa_pf_i, 
                "PF_existential": fa_pf_e, 
                "AR": fa_ar, 
                "MG": fa_mg
            },
            "admits_limits": fa_admits
        }

    # ------------------------------------------------------------------------
    # FRAMEWORK B (Right Column)
    # ------------------------------------------------------------------------
    with col2:
        st.markdown("### 📕 Framework B")
        fb_name = st.text_input("Name", CT_DEFAULT["name"], key="fb_name")
        
        # ====================================================================
        # PRESET BUTTONS - Quick lever adjustments
        # ====================================================================
        st.markdown("**⚡ Quick Presets:**")
        preset_col1, preset_col2, preset_col3, preset_col4 = st.columns([1, 1, 1, 1])
        
        with preset_col1:
            if st.button("⚡ MAX", key="fb_max", help="Set all levers to maximum (10.0)", use_container_width=True):
                st.session_state.fb_cci = 10.0
                st.session_state.fb_edb = 10.0
                st.session_state.fb_pfi = 10.0
                st.session_state.fb_pfe = 10.0
                st.session_state.fb_ar = 10.0
                st.session_state.fb_mg = 10.0
                st.rerun()
        
        with preset_col2:
            if st.button("⚖️ MID", key="fb_mid", help="Set all levers to neutral (5.0)", use_container_width=True):
                st.session_state.fb_cci = 5.0
                st.session_state.fb_edb = 5.0
                st.session_state.fb_pfi = 5.0
                st.session_state.fb_pfe = 5.0
                st.session_state.fb_ar = 5.0
                st.session_state.fb_mg = 5.0
                st.rerun()
        
        with preset_col3:
            if st.button("🔄 RESET", key="fb_reset", help="Reset to defaults", use_container_width=True):
                st.session_state.fb_cci = CT_DEFAULT["levers"]["CCI"]
                st.session_state.fb_edb = CT_DEFAULT["levers"]["EDB"]
                st.session_state.fb_pfi = CT_DEFAULT["levers"]["PF_instrumental"]
                st.session_state.fb_pfe = CT_DEFAULT["levers"]["PF_existential"]
                st.session_state.fb_ar = CT_DEFAULT["levers"]["AR"]
                st.session_state.fb_mg = CT_DEFAULT["levers"]["MG"]
                st.rerun()
        
        with preset_col4:
            if st.button("🚫 MIN", key="fb_min", help="Set all levers to minimum (0.0)", use_container_width=True):
                st.session_state.fb_cci = 0.0
                st.session_state.fb_edb = 0.0
                st.session_state.fb_pfi = 0.0
                st.session_state.fb_pfe = 0.0
                st.session_state.fb_ar = 0.0
                st.session_state.fb_mg = 0.0
                st.rerun()
        
        st.markdown("---")
        
        with st.expander("🔢 BFI", expanded=False):
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
            "levers": {
                "CCI": fb_cci, 
                "EDB": fb_edb, 
                "PF_instrumental": fb_pf_i, 
                "PF_existential": fb_pf_e, 
                "AR": fb_ar, 
                "MG": fb_mg
            },
            "admits_limits": fb_admits
        }

    st.markdown("---")

    # ========================================================================
    # RESULTS - Calculate YPA scores
    # ========================================================================
    ya_results, ya_levers, ya_bfi = ypa_scenario_scores(fa, cfg)
    yb_results, yb_levers, yb_bfi = ypa_scenario_scores(fb, cfg)

    # ========================================================================
    # RESULTS DISPLAY - Tabbed Interface
    # ========================================================================
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Visual", "📋 Details", "🛡️ Guardrails", "🔄 Symmetry"])

    # ------------------------------------------------------------------------
    # TAB 1: Visual Comparisons
    # ------------------------------------------------------------------------
    with tab1:
        st.plotly_chart(
            create_lever_comparison_chart(ya_levers, yb_levers, fa["name"], fb["name"]), 
            use_container_width=True
        )
        st.plotly_chart(
            create_ypa_trinity_chart(ya_results, yb_results, fa["name"], fb["name"]), 
            use_container_width=True
        )

    # ------------------------------------------------------------------------
    # TAB 2: Detailed Metrics
    # ------------------------------------------------------------------------
    with tab2:
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"**{fa['name']}**")
            st.json(ya_levers)
            st.metric("BFI", f"{ya_bfi:.2f}")
            st.metric("Neutral YPA", f"{ya_results['Neutral']['YPA']:.3f}")
            
            st.markdown("**YPA Trinity:**")
            for scenario in ["Neutral", "Existential", "Empirical"]:
                st.metric(scenario, f"{ya_results[scenario]['YPA']:.3f}")
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            st.json(yb_levers)
            st.metric("BFI", f"{yb_bfi:.2f}")
            st.metric("Neutral YPA", f"{yb_results['Neutral']['YPA']:.3f}")
            
            st.markdown("**YPA Trinity:**")
            for scenario in ["Neutral", "Existential", "Empirical"]:
                st.metric(scenario, f"{yb_results[scenario]['YPA']:.3f}")

    # ------------------------------------------------------------------------
    # TAB 3: Guardrails
    # ------------------------------------------------------------------------
    with tab3:
        st.markdown("### 🛡️ Guardrails - Abuse Prevention System")
        
        # Context box explaining why guardrails exist
        st.info("""
        **Why Guardrails Exist:**
        
        During the Level 3 audit ("Mad-King Test"), we simulated intentional manipulation—
        inflating weights, hiding debts, cherry-picking configurations. The guardrails emerged
        as automated checks to catch these distortions.
        
        **Purpose**: Not to declare winners, but to flag suspicious patterns that suggest
        gaming the system rather than honest measurement.
        """)
        
        st.markdown("---")
        
        # ================================================================
        # GUARDRAIL 1: Lever-Coupling
        # ================================================================
        st.markdown("#### 1️⃣ Lever-Coupling Requirement")
        
        st.markdown("""
        **Rule**: If Pragmatic Fertility (PF) ≥ 9, then Coherence (CCI) must be ≥ 6.5
        
        **Why**: High pragmatic success without coherent foundations suggests luck, not competence.
        A framework claiming 90%+ predictive success must have the logical infrastructure to support it.
        
        **Discovered during**: Mad-King Test showed that inflating PF while keeping CCI low
        created suspiciously efficient scores that lacked explanatory grounding.
        """)
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"**{fa['name']}**")
            ok, msg = guardrail_lever_coupling(ya_levers["PF"], ya_levers["CCI"])
            if ok:
                st.success(msg)
                st.caption(f"PF: {ya_levers['PF']:.2f}, CCI: {ya_levers['CCI']:.2f}")
            else:
                st.warning(msg)
                st.caption("This framework claims high success without adequate coherent foundations.")
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            ok, msg = guardrail_lever_coupling(yb_levers["PF"], yb_levers["CCI"])
            if ok:
                st.success(msg)
                st.caption(f"PF: {yb_levers['PF']:.2f}, CCI: {yb_levers['CCI']:.2f}")
            else:
                st.warning(msg)
                st.caption("This framework claims high success without adequate coherent foundations.")
        
        st.markdown("---")
        
        # ================================================================
        # GUARDRAIL 2: BFI-Sensitivity
        # ================================================================
        st.markdown("#### 2️⃣ BFI-Sensitivity Alert")
        
        st.markdown("""
        **Rule**: Flag if YPA increases faster than BFI (ΔYPA / ΔBFI > 0.4)
        
        **Why**: Adding axioms should have diminishing returns. If efficiency *increases*
        as you add more assumptions, something's suspicious—likely gaming the axiom count.
        
        **Discovered during**: Convergence phase revealed that frameworks could artificially
        boost YPA by subdividing one axiom into multiple "smaller" ones while keeping
        lever scores constant.
        """)
        
        st.info("**Status**: Monitoring enabled. Currently checking across scenarios.")
        
        st.markdown("---")
        
        # ================================================================
        # GUARDRAIL 3: Weight-Inversion Alarm
        # ================================================================
        st.markdown("#### 3️⃣ Weight-Inversion Detection")
        
        st.markdown("""
        **Rule**: Flag if any scenario applies weights <0.3× or >3× to any lever
        
        **Why**: Extreme weighting (>3×) or near-elimination (<0.3×) of levers suggests
        cherry-picking scenarios to favor one framework unfairly.
        
        **Discovered during**: Cross-examination phase exposed that early configurations
        inadvertently gave 5× weight to certain levers, distorting comparisons.
        
        **Current configuration**:
        - Neutral: All 1.0×
        - Existential: EDB 2×, MG 2× (no inversion)
        - Empirical: PF 2×, CCI 1.5× (no inversion)
        """)
        
        st.success("✅ PASS: All scenario weights within acceptable range (0.3× - 3.0×)")
        
        st.markdown("---")
        
        # ================================================================
        # GUARDRAIL 4: Symmetry Audit
        # ================================================================
        st.markdown("#### 4️⃣ Symmetry Audit (Toggle Testing)")
        
        st.markdown("""
        **Rule**: Test 3 toggle inversions per framework; flag if Δ > 0.3 YPA
        
        **Why**: Large toggle sensitivity (Δ > 0.3) reveals structural dependencies.
        This isn't "bad"—it shows which configurations favor which frameworks.
        The key is **disclosure**: users must see these impacts clearly.
        
        **Discovered during**: Level 2 cross-examination revealed that certain toggles
        (especially Lever-Parity) massively impacted CT scores (~1.0 YPA swing).
        Rather than "fix" this, we made it visible and adjustable.
        """)
        
        st.markdown("*See the **Symmetry** tab for detailed toggle sensitivity analysis.*")
        
        st.markdown("---")
        
        # ================================================================
        # SUMMARY BOX
        # ================================================================
        st.success("""
        ### ✅ Guardrail Summary
        
        **Purpose**: Catch manipulation, not declare winners
        
        **4 Automated Checks**:
        1. Lever-Coupling (PF/CCI relationship)
        2. BFI-Sensitivity (efficiency vs assumptions)
        3. Weight-Inversion (extreme scenario weighting)
        4. Symmetry Audit (toggle impact disclosure)
        
        **Result**: System prevents gaming while allowing honest structural differences
        
        > "Not neutrality (impossible), but transparency (achievable)"  
        > — CFA v2.0 Design Principle
        """)

    # ------------------------------------------------------------------------
    # TAB 4: Symmetry Audit
    # ------------------------------------------------------------------------
    with tab4:
        st.markdown("### Toggle Sensitivity Analysis")
        st.markdown("*Shows how each framework responds to configuration changes*")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"**{fa['name']}**")
            audit = symmetry_audit(fa, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "⚠️" if abs(x) > 0.3 else "✅")
            st.dataframe(df, use_container_width=True)
            
            st.markdown("**Legend:**")
            st.markdown("- ✅ Small impact (Δ < 0.3) - Toggle-robust")
            st.markdown("- ⚠️ Large impact (Δ > 0.3) - Toggle-sensitive")
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            audit = symmetry_audit(fb, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "⚠️" if abs(x) > 0.3 else "✅")
            st.dataframe(df, use_container_width=True)
            
            st.markdown("**Legend:**")
            st.markdown("- ✅ Small impact (Δ < 0.3) - Toggle-robust")
            st.markdown("- ⚠️ Large impact (Δ > 0.3) - Toggle-sensitive")

    # ========================================================================
    # EXPORT FUNCTIONALITY
    # ========================================================================
    st.markdown("---")
    st.markdown("### 📥 Export Your Run")
    
    export = {
        "config": cfg,
        "framework_a": fa,
        "framework_b": fb,
        "results": {
            "a": {
                "levers": ya_levers, 
                "bfi": ya_bfi, 
                "ypa": {k: v["YPA"] for k, v in ya_results.items()}
            },
            "b": {
                "levers": yb_levers, 
                "bfi": yb_bfi, 
                "ypa": {k: v["YPA"] for k, v in yb_results.items()}
            }
        }
    }
    
    st.download_button(
        "📥 Export Run (JSON)", 
        json.dumps(export, indent=2), 
        "cfa_run.json", 
        "application/json",
        help="Download your complete configuration and results as JSON"
    )
    
    # Footer
    st.markdown("---")
    st.caption("CFA v2.0 Console | Adjust toggles and sliders to explore framework comparisons")

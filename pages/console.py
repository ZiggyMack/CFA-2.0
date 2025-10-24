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
        st.markdown("### Lever-Coupling Guardrail")
        st.markdown("*High pragmatic success (PF ≥ 9) must be backed by coherent foundations (CCI ≥ 6.5)*")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"**{fa['name']}**")
            ok, msg = guardrail_lever_coupling(ya_levers["PF"], ya_levers["CCI"])
            if ok:
                st.success(msg)
            else:
                st.warning(msg)
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            ok, msg = guardrail_lever_coupling(yb_levers["PF"], yb_levers["CCI"])
            if ok:
                st.success(msg)
            else:
                st.warning(msg)

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

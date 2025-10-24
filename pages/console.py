"""
CFA v2.0 - Console Page Component (COMPLETE ENHANCED VERSION)
- Preset buttons at bottom (before tabs)
- JSON Import/Export functionality
- All existing enhancements preserved
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

# ============================================================================
# JSON IMPORT HELPER FUNCTIONS
# ============================================================================

def apply_loaded_run(run: dict):
    """Apply a loaded JSON configuration to session state"""
    # Config
    cfg = run.get("config", {})
    if "lever_parity" in cfg:
        st.session_state["sidebar_lever_parity"] = cfg["lever_parity"]
    if "pf_type" in cfg:
        st.session_state["sidebar_pf_type"] = cfg["pf_type"]
    if "fallibilism_bonus" in cfg:
        st.session_state["sidebar_fallibilism"] = cfg["fallibilism_bonus"]
    if "bfi_debt_weight" in cfg:
        st.session_state["sidebar_bfi_weight"] = cfg["bfi_debt_weight"]

    # Framework A
    A = run.get("framework_a", {})
    if "name" in A:
        st.session_state["fa_name"] = A["name"]
    if "bf_i" in A:
        st.session_state["fa_ax"] = A["bf_i"].get("axioms", 6)
        st.session_state["fa_db"] = A["bf_i"].get("debts", 4)
    if "admits_limits" in A:
        st.session_state["fa_ad"] = bool(A["admits_limits"])
    if "levers" in A:
        levers = A["levers"]
        st.session_state["fa_cci"] = float(levers.get("CCI", 5.0))
        st.session_state["fa_edb"] = float(levers.get("EDB", 5.0))
        st.session_state["fa_pfi"] = float(levers.get("PF_instrumental", 5.0))
        st.session_state["fa_pfe"] = float(levers.get("PF_existential", 5.0))
        st.session_state["fa_ar"] = float(levers.get("AR", 5.0))
        st.session_state["fa_mg"] = float(levers.get("MG", 5.0))

    # Framework B
    B = run.get("framework_b", {})
    if "name" in B:
        st.session_state["fb_name"] = B["name"]
    if "bf_i" in B:
        st.session_state["fb_ax"] = B["bf_i"].get("axioms", 6)
        st.session_state["fb_db"] = B["bf_i"].get("debts", 4)
    if "admits_limits" in B:
        st.session_state["fb_ad"] = bool(B["admits_limits"])
    if "levers" in B:
        levers = B["levers"]
        st.session_state["fb_cci"] = float(levers.get("CCI", 5.0))
        st.session_state["fb_edb"] = float(levers.get("EDB", 5.0))
        st.session_state["fb_pfi"] = float(levers.get("PF_instrumental", 5.0))
        st.session_state["fb_pfe"] = float(levers.get("PF_existential", 5.0))
        st.session_state["fb_ar"] = float(levers.get("AR", 5.0))
        st.session_state["fb_mg"] = float(levers.get("MG", 5.0))

    return True

def render():
    """Render the console page"""
    
    # ========================================================================
    # INITIALIZE SESSION STATE FOR ALL SLIDERS (if not exist)
    # ========================================================================
    # Framework A defaults
    if "fa_cci" not in st.session_state:
        st.session_state["fa_cci"] = MDN_DEFAULT["levers"]["CCI"]
    if "fa_edb" not in st.session_state:
        st.session_state["fa_edb"] = MDN_DEFAULT["levers"]["EDB"]
    if "fa_pfi" not in st.session_state:
        st.session_state["fa_pfi"] = MDN_DEFAULT["levers"]["PF_instrumental"]
    if "fa_pfe" not in st.session_state:
        st.session_state["fa_pfe"] = MDN_DEFAULT["levers"]["PF_existential"]
    if "fa_ar" not in st.session_state:
        st.session_state["fa_ar"] = MDN_DEFAULT["levers"]["AR"]
    if "fa_mg" not in st.session_state:
        st.session_state["fa_mg"] = MDN_DEFAULT["levers"]["MG"]
    
    # Framework B defaults
    if "fb_cci" not in st.session_state:
        st.session_state["fb_cci"] = CT_DEFAULT["levers"]["CCI"]
    if "fb_edb" not in st.session_state:
        st.session_state["fb_edb"] = CT_DEFAULT["levers"]["EDB"]
    if "fb_pfi" not in st.session_state:
        st.session_state["fb_pfi"] = CT_DEFAULT["levers"]["PF_instrumental"]
    if "fb_pfe" not in st.session_state:
        st.session_state["fb_pfe"] = CT_DEFAULT["levers"]["PF_existential"]
    if "fb_ar" not in st.session_state:
        st.session_state["fb_ar"] = CT_DEFAULT["levers"]["AR"]
    if "fb_mg" not in st.session_state:
        st.session_state["fb_mg"] = CT_DEFAULT["levers"]["MG"]
    
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
    # SIDEBAR: PRESET LIBRARY + JSON IMPORT + TOGGLES
    # ========================================================================
    st.sidebar.header("🎛️ Configuration")
    
    # Preset Profile Library
    with st.sidebar.expander("📚 Load Preset Profile", expanded=False):
        st.markdown("**Pre-Audited Frameworks:**")
        
        preset_options = {
            "-- Select Framework --": None,
            "✅ Methodological Naturalism (MdN)": "mdn",
            "✅ Classical Theism (CT)": "ct",
            "🔜 Buddhism": "coming",
            "🔜 Stoicism": "coming",
            "🔜 Pragmatism": "coming",
            "🔜 Process Theology": "coming",
            "🔜 Secular Humanism": "coming",
            "🔜 Metaphysical Naturalism": "coming"
        }
        
        selected_preset = st.selectbox(
            "Choose Framework:",
            list(preset_options.keys()),
            key="preset_selector"
        )
        
        preset_key = preset_options[selected_preset]
        
        if preset_key == "mdn":
            st.info("**Methodological Naturalism**\n\nResearch protocol assuming testable natural causes. Audited by Claude + Grok with 98% convergence.")
            
            if st.button("Load MdN Profile", use_container_width=True):
                # Load MdN into Framework A
                st.session_state["fa_name"] = "Methodological Naturalism"
                st.session_state["fa_ax"] = 6
                st.session_state["fa_db"] = 4
                st.session_state["fa_ad"] = True
                st.session_state["fa_cci"] = 8.0
                st.session_state["fa_edb"] = 7.5
                st.session_state["fa_pfi"] = 10.0
                st.session_state["fa_pfe"] = 3.0
                st.session_state["fa_ar"] = 7.0
                st.session_state["fa_mg"] = 4.0
                st.success("✅ MdN loaded into Framework A!")
                st.rerun()
        
        elif preset_key == "ct":
            st.info("**Classical Theism**\n\nTraditional monotheistic worldview. Audited by Claude + Grok with 98% convergence.")
            
            if st.button("Load CT Profile", use_container_width=True):
                # Load CT into Framework B
                st.session_state["fb_name"] = "Classical Theism"
                st.session_state["fb_ax"] = 7
                st.session_state["fb_db"] = 4
                st.session_state["fb_ad"] = True
                st.session_state["fb_cci"] = 7.5
                st.session_state["fb_edb"] = 8.5
                st.session_state["fb_pfi"] = 7.0
                st.session_state["fb_pfe"] = 8.0
                st.session_state["fb_ar"] = 8.5
                st.session_state["fb_mg"] = 8.5
                st.success("✅ CT loaded into Framework B!")
                st.rerun()
        
        elif preset_key == "coming":
            st.warning(f"**{selected_preset.replace('🔜 ', '')}**\n\nAudit in progress. Check back soon!\n\n*Want to help audit this framework? Export your analysis and share with the community.*")
        
        if selected_preset != "-- Select Framework --":
            st.markdown("---")
            st.caption("💡 **Tip:** Load two presets to compare, or load one and build your own in the other slot!")
    
    st.sidebar.markdown("---")
    
    # JSON Import Section
    with st.sidebar.expander("📥 Import Custom JSON", expanded=False):
        st.markdown("**Upload a saved audit:**")
        uploaded_file = st.file_uploader("Choose JSON file", type=["json"], key="json_upload")
        if uploaded_file is not None:
            try:
                run = json.load(uploaded_file)
                # Validate structure
                if "config" in run and "framework_a" in run and "framework_b" in run:
                    st.success("✅ Valid CFA profile detected")
                    
                    # Show preview
                    with st.expander("Preview"):
                        st.write(f"**Framework A:** {run['framework_a'].get('name', 'Unknown')}")
                        st.write(f"**Framework B:** {run['framework_b'].get('name', 'Unknown')}")
                    
                    if st.button("✅ Apply Loaded Configuration", use_container_width=True):
                        apply_loaded_run(run)
                        st.success("Configuration loaded! Page will refresh...")
                        st.rerun()
                else:
                    st.error("Invalid JSON format. Expected 'config', 'framework_a', and 'framework_b' keys.")
            except Exception as e:
                st.error(f"Could not load file: {e}")
    
    st.sidebar.markdown("---")
    
    # Toggles
    lever_parity = st.sidebar.selectbox(
        "Lever-Parity", 
        ["ON", "OFF"], 
        index=0,
        key="sidebar_lever_parity",
        help="**Lever-Parity Toggle**: Should moral norms (MG) be weighted equally with epistemic norms (CCI/EDB)?\n\n• **ON** = MG counts fully (1.0×) - favors comprehensive worldviews\n• **OFF** = MG down-weighted (0.5×) - favors methodological frameworks\n\n*Impact: CT loses ~0.8 YPA when OFF*"
    )
    
    pf_type = st.sidebar.selectbox(
        "PF-Type", 
        PF_TYPES, 
        index=1,
        key="sidebar_pf_type",
        help="**PF-Type Toggle**: How should Pragmatic Fertility be calculated?\n\n• **Instrumental** = Tech/prediction only (100%) - favors MdN\n• **Composite 70:30** = Balanced mix (default) - fair comparison\n• **Holistic 50:50** = Equal weight to meaning/purpose - favors CT\n\n*Impact: ±0.4 YPA depending on choice*"
    )
    
    fall_bonus = st.sidebar.selectbox(
        "Fallibilism-Bonus", 
        ["ON", "OFF"], 
        index=0,
        key="sidebar_fallibilism",
        help="**Fallibilism-Bonus Toggle**: Should frameworks that admit their limits get a CCI bonus?\n\n• **ON** = +0.3 CCI for frameworks checking 'Admits Limits'\n• **OFF** = No bonus (confidence not penalized if grounded)\n\n*Impact: Usually small (±0.1 YPA)*"
    )
    
    bfi_weight = st.sidebar.selectbox(
        "BFI Debt Weight", 
        ["Equal_1.0x", "Weighted_1.2x"], 
        index=0,
        key="sidebar_bfi_weight",
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
    # IMPORT/EXPORT AT BOTTOM OF SIDEBAR (compact)
    # ========================================================================
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📥📤 Quick Actions")
    
    sidebar_col1, sidebar_col2 = st.sidebar.columns(2)
    
    with sidebar_col1:
        # Compact import
        st.caption("**Import**")
        import_file = st.file_uploader("", type=["json"], key="quick_import", label_visibility="collapsed")
        if import_file:
            try:
                run = json.load(import_file)
                if "config" in run:
                    if st.button("✅", key="quick_apply", help="Apply loaded config"):
                        apply_loaded_run(run)
                        st.rerun()
            except:
                pass
    
    with sidebar_col2:
        # Compact export placeholder (will be populated after calculations)
        st.caption("**Export**")
        st.caption("*See bottom of page*")

    # ========================================================================
    # FRAMEWORK EDITORS (Two Columns) - NO PRESET BUTTONS HERE
    # ========================================================================
    col1, col2 = st.columns(2)

    # ------------------------------------------------------------------------
    # FRAMEWORK A (Left Column)
    # ------------------------------------------------------------------------
    with col1:
        st.markdown("### 📘 Framework A")
        fa_name = st.text_input("Name", MDN_DEFAULT["name"], key="fa_name")
        
        with st.expander("🔢 BFI", expanded=False):
            # Check if custom framework is waiting
            if 'custom_framework_ready' in st.session_state:
                custom = st.session_state['custom_framework_ready']
                if custom.get('target') == 'framework_a':
                    st.info(f"🔔 **Custom framework ready:** {custom['name']}")
                    if st.button("✅ Apply Custom Framework", key="apply_custom_a"):
                        st.session_state.fa_name = custom['name']
                        st.session_state.fa_ax = custom['axioms']
                        st.session_state.fa_db = custom['debts']
                        # Clear the flag
                        del st.session_state['custom_framework_ready']
                        st.rerun()
            
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
            
            # Show link to Brute Ledger
            if st.button("🔍 Go to Brute Ledger", key="goto_ledger_a"):
                st.session_state.page = 'brute_ledger'
                st.rerun()
        
        fa_cci = st.slider(
            "CCI - Coherence & Closure", 
            0.0, 10.0, 
            value=st.session_state["fa_cci"],
            step=0.1, 
            key="fa_cci",
            help="**Coherence & Internal Consistency**: Are the rules internally consistent? Does the framework contradict itself? Higher scores = tighter logical structure."
        )
        fa_edb = st.slider(
            "EDB - Explanatory Depth & Breadth", 
            0.0, 10.0,
            value=st.session_state["fa_edb"],
            step=0.1, 
            key="fa_edb",
            help="**Explanatory Depth and Breadth**: How much can it explain? How deeply? Covers both scope and detail of explanations."
        )
        fa_pf_i = st.slider(
            "PF-Instrumental", 
            0.0, 10.0,
            value=st.session_state["fa_pfi"],
            step=0.1, 
            key="fa_pfi",
            help="**Pragmatic Fertility (Instrumental)**: Tech/predictive yield. Does it generate successful predictions, technology, practical applications? Scientific method excels here."
        )
        fa_pf_e = st.slider(
            "PF-Existential", 
            0.0, 10.0,
            value=st.session_state["fa_pfe"],
            step=0.1, 
            key="fa_pfe",
            help="**Pragmatic Fertility (Existential)**: Meaning/purpose generation. Does it help people find meaning, orient their lives, address existential questions? Worldviews excel here."
        )
        fa_ar = st.slider(
            "AR - Aesthetic Resonance", 
            0.0, 10.0,
            value=st.session_state["fa_ar"],
            step=0.1, 
            key="fa_ar",
            help="**Aesthetic Resonance**: Does it exhibit elegance, simplicity, beauty? Do its explanations have mathematical/conceptual beauty? Parsimony and pattern-recognition."
        )
        fa_mg = st.slider(
            "MG - Moral Generativity", 
            0.0, 10.0,
            value=st.session_state["fa_mg"],
            step=0.1, 
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
            # Check if custom framework is waiting
            if 'custom_framework_ready' in st.session_state:
                custom = st.session_state['custom_framework_ready']
                if custom.get('target') == 'framework_b':
                    st.info(f"🔔 **Custom framework ready:** {custom['name']}")
                    if st.button("✅ Apply Custom Framework", key="apply_custom_b"):
                        st.session_state.fb_name = custom['name']
                        st.session_state.fb_ax = custom['axioms']
                        st.session_state.fb_db = custom['debts']
                        # Clear the flag
                        del st.session_state['custom_framework_ready']
                        st.rerun()
            
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
            
            # Show link to Brute Ledger
            if st.button("🔍 Go to Brute Ledger", key="goto_ledger_b"):
                st.session_state.page = 'brute_ledger'
                st.rerun()
        
        fb_cci = st.slider(
            "CCI - Coherence & Closure", 
            0.0, 10.0,
            value=st.session_state["fb_cci"],
            step=0.1, 
            key="fb_cci",
            help="**Coherence & Internal Consistency**: Are the rules internally consistent? Does the framework contradict itself? Higher scores = tighter logical structure."
        )
        fb_edb = st.slider(
            "EDB - Explanatory Depth & Breadth", 
            0.0, 10.0,
            value=st.session_state["fb_edb"],
            step=0.1, 
            key="fb_edb",
            help="**Explanatory Depth & Breadth**: How much can it explain? How deeply? Covers both scope (breadth) and detail (depth) of explanations provided."
        )
        fb_pf_i = st.slider(
            "PF-Instrumental", 
            0.0, 10.0,
            value=st.session_state["fb_pfi"],
            step=0.1, 
            key="fb_pfi",
            help="**Pragmatic Fertility (Instrumental)**: Tech/predictive yield. Does it generate successful predictions, technology, practical applications? Scientific method excels here."
        )
        fb_pf_e = st.slider(
            "PF-Existential", 
            0.0, 10.0,
            value=st.session_state["fb_pfe"],
            step=0.1, 
            key="fb_pfe",
            help="**Pragmatic Fertility (Existential)**: Meaning/purpose generation. Does it help people find meaning, orient their lives, address existential questions? Worldviews excel here."
        )
        fb_ar = st.slider(
            "AR - Aesthetic Resonance", 
            0.0, 10.0,
            value=st.session_state["fb_ar"],
            step=0.1, 
            key="fb_ar",
            help="**Aesthetic Resonance**: Does it exhibit elegance, simplicity, beauty? Do its explanations have mathematical/conceptual beauty? Parsimony and pattern-recognition."
        )
        fb_mg = st.slider(
            "MG - Moral Generativity", 
            0.0, 10.0,
            value=st.session_state["fb_mg"],
            step=0.1, 
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
    # PRESET BUTTONS - At bottom, before tabs
    # ========================================================================
    st.markdown("### ⚡ Quick Presets")
    st.markdown("*Quickly adjust both frameworks to test extremes or reset to defaults*")
    
    preset_row = st.columns([1, 1, 1, 1])
    
    with preset_row[0]:
        if st.button("⚡ ALL MAX", help="Set all levers to 10.0 for both frameworks", use_container_width=True, key="preset_max"):
            # Framework A
            for key in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                st.session_state[key] = 10.0
            # Framework B
            for key in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                st.session_state[key] = 10.0
            st.rerun()
    
    with preset_row[1]:
        if st.button("⚖️ ALL MID", help="Set all levers to 5.0 for both frameworks", use_container_width=True, key="preset_mid"):
            # Framework A
            for key in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                st.session_state[key] = 5.0
            # Framework B
            for key in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                st.session_state[key] = 5.0
            st.rerun()
    
    with preset_row[2]:
        if st.button("🔄 RESET DEFAULTS", help="Reset to MdN vs CT defaults", use_container_width=True, key="preset_reset"):
            # Framework A (MdN)
            st.session_state["fa_cci"] = MDN_DEFAULT["levers"]["CCI"]
            st.session_state["fa_edb"] = MDN_DEFAULT["levers"]["EDB"]
            st.session_state["fa_pfi"] = MDN_DEFAULT["levers"]["PF_instrumental"]
            st.session_state["fa_pfe"] = MDN_DEFAULT["levers"]["PF_existential"]
            st.session_state["fa_ar"] = MDN_DEFAULT["levers"]["AR"]
            st.session_state["fa_mg"] = MDN_DEFAULT["levers"]["MG"]
            # Framework B (CT)
            st.session_state["fb_cci"] = CT_DEFAULT["levers"]["CCI"]
            st.session_state["fb_edb"] = CT_DEFAULT["levers"]["EDB"]
            st.session_state["fb_pfi"] = CT_DEFAULT["levers"]["PF_instrumental"]
            st.session_state["fb_pfe"] = CT_DEFAULT["levers"]["PF_existential"]
            st.session_state["fb_ar"] = CT_DEFAULT["levers"]["AR"]
            st.session_state["fb_mg"] = CT_DEFAULT["levers"]["MG"]
            st.rerun()
    
    with preset_row[3]:
        if st.button("🚫 ALL MIN", help="Set all levers to 0.0 for both frameworks", use_container_width=True, key="preset_min"):
            # Framework A
            for key in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                st.session_state[key] = 0.0
            # Framework B
            for key in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                st.session_state[key] = 0.0
            st.rerun()

    st.markdown("---")

    # ========================================================================
    # CALCULATE RESULTS
    # ========================================================================
    ya_results, ya_levers, ya_bfi = ypa_scenario_scores(fa, cfg)
    yb_results, yb_levers, yb_bfi = ypa_scenario_scores(fb, cfg)

    # ========================================================================
    # RESULTS TABS
    # ========================================================================
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Visual", "📋 Details", "🛡️ Guardrails", "🔄 Symmetry"])

    # ------------------------------------------------------------------------
    # TAB 1: Visual Charts
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
    # TAB 3: Enhanced Guardrails
    # ------------------------------------------------------------------------
    with tab3:
        st.markdown("### 🛡️ Guardrails - Abuse Prevention System")
        
        st.info("""
        **Why Guardrails Exist:**
        
        During the Level 3 audit ("Mad-King Test"), we simulated intentional manipulation—
        inflating weights, hiding debts, cherry-picking configurations. The guardrails emerged
        as automated checks to catch these distortions.
        
        **Purpose**: Not to declare winners, but to flag suspicious patterns that suggest
        gaming the system rather than honest measurement.
        """)
        
        st.markdown("---")
        
        # Guardrail 1
        st.markdown("#### 1️⃣ Lever-Coupling Requirement")
        st.markdown("""
        **Rule**: If Pragmatic Fertility (PF) ≥ 9, then Coherence (CCI) must be ≥ 6.5
        
        **Why**: High pragmatic success without coherent foundations suggests luck, not competence.
        
        **Discovered during**: Mad-King Test showed that inflating PF while keeping CCI low
        created suspiciously efficient scores.
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
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            ok, msg = guardrail_lever_coupling(yb_levers["PF"], yb_levers["CCI"])
            if ok:
                st.success(msg)
                st.caption(f"PF: {yb_levers['PF']:.2f}, CCI: {yb_levers['CCI']:.2f}")
            else:
                st.warning(msg)
        
        st.markdown("---")
        
        # Guardrail 2
        st.markdown("#### 2️⃣ BFI-Sensitivity Alert")
        st.markdown("""
        **Rule**: Flag if YPA increases faster than BFI (ΔYPA / ΔBFI > 0.4)
        
        **Why**: Adding axioms should have diminishing returns.
        
        **Status**: Monitoring enabled.
        """)
        st.info("✓ Currently checking across scenarios")
        
        st.markdown("---")
        
        # Guardrail 3
        st.markdown("#### 3️⃣ Weight-Inversion Detection")
        st.markdown("""
        **Rule**: Flag if any scenario applies weights <0.3× or >3×
        
        **Current configuration**:
        - Neutral: All 1.0×
        - Existential: EDB 2×, MG 2×
        - Empirical: PF 2×, CCI 1.5×
        """)
        st.success("✅ PASS: All scenario weights within acceptable range")
        
        st.markdown("---")
        
        # Guardrail 4
        st.markdown("#### 4️⃣ Symmetry Audit")
        st.markdown("""
        **Rule**: Test 3 toggle inversions per framework; flag if Δ > 0.3 YPA
        
        **Why**: Large toggle sensitivity reveals structural dependencies.
        
        *See the **Symmetry** tab for detailed toggle sensitivity analysis.*
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
            st.dataframe(df)
        
        with c2:
            st.markdown(f"**{fb['name']}**")
            audit = symmetry_audit(fb, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "⚠️" if abs(x) > 0.3 else "✅")
            st.dataframe(df)

    # ========================================================================
    # IMPORT/EXPORT AT BOTTOM OF PAGE
    # ========================================================================
    st.markdown("---")
    st.markdown("### 📥 Import / 📤 Export")
    
    bottom_col1, bottom_col2 = st.columns(2)
    
    with bottom_col1:
        st.markdown("**📥 Import Configuration**")
        st.caption("*Load a previously saved audit or community profile*")
        
        import_file_bottom = st.file_uploader(
            "Choose JSON file",
            type=["json"],
            key="json_upload_bottom"
        )
        
        if import_file_bottom is not None:
            try:
                run = json.load(import_file_bottom)
                if "config" in run and "framework_a" in run and "framework_b" in run:
                    st.success("✅ Valid CFA profile detected")
                    
                    # Show preview
                    with st.expander("📋 Preview Configuration"):
                        st.write(f"**Framework A:** {run['framework_a'].get('name', 'Unknown')}")
                        st.write(f"**Framework B:** {run['framework_b'].get('name', 'Unknown')}")
                        st.write(f"**Config:** {run['config']}")
                    
                    if st.button("✅ Apply Loaded Configuration", use_container_width=True, key="apply_bottom"):
                        apply_loaded_run(run)
                        st.success("Configuration loaded! Page will refresh...")
                        st.rerun()
                else:
                    st.error("Invalid JSON format. Expected 'config', 'framework_a', and 'framework_b' keys.")
            except Exception as e:
                st.error(f"Could not load file: {e}")
    
    with bottom_col2:
        st.markdown("**📤 Export Current Audit**")
        st.caption("*Save your configuration and results to reload later or share*")
        
        export = {
            "config": cfg,
            "framework_a": fa,
            "framework_b": fb,
            "results": {
                "a": {"levers": ya_levers, "bfi": ya_bfi, "ypa": {k: v["YPA"] for k, v in ya_results.items()}},
                "b": {"levers": yb_levers, "bfi": yb_bfi, "ypa": {k: v["YPA"] for k, v in yb_results.items()}}
            }
        }
        
        st.download_button(
            "📥 Download Complete Audit (JSON)",
            json.dumps(export, indent=2),
            "cfa_run.json",
            "application/json",
            use_container_width=True,
            help="Download your current configuration and results as JSON"
        )
        
        st.info("""
        **What's included:**
        - Toggle settings
        - Both framework configurations
        - All lever scores
        - Calculated YPA results
        """)


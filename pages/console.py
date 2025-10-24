"""
CFA v2.0 - Console (FIXED VERSION)
Version: 2.0.1  # <-- Change this number
- Per-framework preset buttons ABOVE sliders
"""
CFA v2.0 - Console (FIXED VERSION)
- Per-framework preset buttons ABOVE sliders
- Global preset buttons removed (they break when below)
- Sidebar simplified (just Import at bottom)
- Bottom page has Import + Export side-by-side
"""

import streamlit as st
import pandas as pd
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.calculations import ypa_scenario_scores, guardrail_lever_coupling, symmetry_audit, PF_TYPES
from utils.visualizations import create_lever_comparison_chart, create_ypa_trinity_chart
from utils.frameworks import MDN_DEFAULT, CT_DEFAULT

def apply_loaded_run(run: dict):
    """Apply loaded JSON to session state"""
    cfg = run.get("config", {})
    if "lever_parity" in cfg:
        st.session_state["sidebar_lever_parity"] = cfg["lever_parity"]
    if "pf_type" in cfg:
        st.session_state["sidebar_pf_type"] = cfg["pf_type"]
    if "fallibilism_bonus" in cfg:
        st.session_state["sidebar_fallibilism"] = cfg["fallibilism_bonus"]
    if "bfi_debt_weight" in cfg:
        st.session_state["sidebar_bfi_weight"] = cfg["bfi_debt_weight"]

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

def render():
    """Render console"""
    
    # Initialize session state
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
    
    # Header
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown('<p style="font-size:2.5rem;font-weight:bold;color:#1f77b4;">⚖️ CFA v2.0 Console</p>', unsafe_allow_html=True)
    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = 'landing'
            st.rerun()
    
    st.markdown('**"All Named, All Priced" — Interactive Comparison Tool**')
    st.markdown("---")

    # SIDEBAR
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
            st.warning(f"**{selected_preset.replace('🔜 ', '')}**\n\nAudit in progress. Check back soon!")
        
        if selected_preset != "-- Select Framework --":
            st.markdown("---")
            st.caption("💡 **Tip:** Load two presets to compare!")
    
    st.sidebar.markdown("---")
    
    lever_parity = st.sidebar.selectbox(
        "Lever-Parity", 
        ["ON", "OFF"], 
        index=0,
        key="sidebar_lever_parity",
        help="**Lever-Parity Toggle**: Should moral norms (MG) be weighted equally with epistemic norms?"
    )
    
    pf_type = st.sidebar.selectbox(
        "PF-Type", 
        PF_TYPES, 
        index=1,
        key="sidebar_pf_type",
        help="**PF-Type Toggle**: How should Pragmatic Fertility be calculated?"
    )
    
    fall_bonus = st.sidebar.selectbox(
        "Fallibilism-Bonus", 
        ["ON", "OFF"], 
        index=0,
        key="sidebar_fallibilism",
        help="**Fallibilism-Bonus Toggle**: Should frameworks that admit limits get CCI bonus?"
    )
    
    bfi_weight = st.sidebar.selectbox(
        "BFI Debt Weight", 
        ["Equal_1.0x", "Weighted_1.2x"], 
        index=0,
        key="sidebar_bfi_weight",
        help="**BFI Debt Weighting**: Should debts cost more than axioms?"
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
    
    # Sidebar Import only
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📥 Import")
    import_file_sidebar = st.sidebar.file_uploader("Load saved audit", type=["json"], key="import_sidebar")
    if import_file_sidebar:
        try:
            run = json.load(import_file_sidebar)
            if "config" in run:
                if st.sidebar.button("✅ Apply", key="apply_sidebar"):
                    apply_loaded_run(run)
                    st.rerun()
        except:
            st.sidebar.error("Invalid file")

    # FRAMEWORK EDITORS
    col1, col2 = st.columns(2)

    # FRAMEWORK A
    with col1:
        st.markdown("### 📘 Framework A")
        fa_name = st.text_input("Name", MDN_DEFAULT["name"], key="fa_name")
        
        with st.expander("🔢 BFI", expanded=False):
            if 'custom_framework_ready' in st.session_state:
                custom = st.session_state['custom_framework_ready']
                if custom.get('target') == 'framework_a':
                    st.info(f"🔔 **Custom framework ready:** {custom['name']}")
                    if st.button("✅ Apply Custom Framework", key="apply_custom_a"):
                        st.session_state.fa_name = custom['name']
                        st.session_state.fa_ax = custom['axioms']
                        st.session_state.fa_db = custom['debts']
                        del st.session_state['custom_framework_ready']
                        st.rerun()
            
            fa_axioms = st.number_input("Axioms", 1, 30, MDN_DEFAULT["bf_i"]["axioms"], key="fa_ax")
            fa_debts = st.number_input("Debts", 0, 30, MDN_DEFAULT["bf_i"]["debts"], key="fa_db")
            fa_admits = st.checkbox("Admits Limits", True, key="fa_ad")
            
            if st.button("🔍 Go to Brute Ledger", key="goto_ledger_a"):
                st.session_state.page = 'brute_ledger'
                st.rerun()
        
        # SLIDERS
        fa_cci = st.slider("CCI - Coherence & Closure", 0.0, 10.0, value=st.session_state["fa_cci"], step=0.1, key="fa_cci")
        fa_edb = st.slider("EDB - Explanatory Depth & Breadth", 0.0, 10.0, value=st.session_state["fa_edb"], step=0.1, key="fa_edb")
        fa_pf_i = st.slider("PF-Instrumental", 0.0, 10.0, value=st.session_state["fa_pfi"], step=0.1, key="fa_pfi")
        fa_pf_e = st.slider("PF-Existential", 0.0, 10.0, value=st.session_state["fa_pfe"], step=0.1, key="fa_pfe")
        fa_ar = st.slider("AR - Aesthetic Resonance", 0.0, 10.0, value=st.session_state["fa_ar"], step=0.1, key="fa_ar")
        fa_mg = st.slider("MG - Moral Generativity", 0.0, 10.0, value=st.session_state["fa_mg"], step=0.1, key="fa_mg")
        
        # PER-FRAMEWORK PRESET BUTTONS (BELOW SLIDERS - small)
        st.caption("**⚡ Quick Adjust:**")
        preset_a = st.columns(4)
        with preset_a[0]:
            if st.button("MAX", key="fa_max_btn", help="Set all to 10.0"):
                for k in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                    st.session_state[k] = 10.0
                st.rerun()
        with preset_a[1]:
            if st.button("MID", key="fa_mid_btn", help="Set all to 5.0"):
                for k in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                    st.session_state[k] = 5.0
                st.rerun()
        with preset_a[2]:
            if st.button("RESET", key="fa_reset_btn", help="Reset to MdN"):
                st.session_state["fa_cci"] = MDN_DEFAULT["levers"]["CCI"]
                st.session_state["fa_edb"] = MDN_DEFAULT["levers"]["EDB"]
                st.session_state["fa_pfi"] = MDN_DEFAULT["levers"]["PF_instrumental"]
                st.session_state["fa_pfe"] = MDN_DEFAULT["levers"]["PF_existential"]
                st.session_state["fa_ar"] = MDN_DEFAULT["levers"]["AR"]
                st.session_state["fa_mg"] = MDN_DEFAULT["levers"]["MG"]
                st.rerun()
        with preset_a[3]:
            if st.button("MIN", key="fa_min_btn", help="Set all to 0.0"):
                for k in ["fa_cci", "fa_edb", "fa_pfi", "fa_pfe", "fa_ar", "fa_mg"]:
                    st.session_state[k] = 0.0
                st.rerun()

        fa = {
            "name": fa_name,
            "bf_i": {"axioms": fa_axioms, "debts": fa_debts},
            "levers": {"CCI": fa_cci, "EDB": fa_edb, "PF_instrumental": fa_pf_i, "PF_existential": fa_pf_e, "AR": fa_ar, "MG": fa_mg},
            "admits_limits": fa_admits
        }

    # FRAMEWORK B
    with col2:
        st.markdown("### 📕 Framework B")
        fb_name = st.text_input("Name", CT_DEFAULT["name"], key="fb_name")
        
        with st.expander("🔢 BFI", expanded=False):
            if 'custom_framework_ready' in st.session_state:
                custom = st.session_state['custom_framework_ready']
                if custom.get('target') == 'framework_b':
                    st.info(f"🔔 **Custom framework ready:** {custom['name']}")
                    if st.button("✅ Apply Custom Framework", key="apply_custom_b"):
                        st.session_state.fb_name = custom['name']
                        st.session_state.fb_ax = custom['axioms']
                        st.session_state.fb_db = custom['debts']
                        del st.session_state['custom_framework_ready']
                        st.rerun()
            
            fb_axioms = st.number_input("Axioms", 1, 30, CT_DEFAULT["bf_i"]["axioms"], key="fb_ax")
            fb_debts = st.number_input("Debts", 0, 30, CT_DEFAULT["bf_i"]["debts"], key="fb_db")
            fb_admits = st.checkbox("Admits Limits", True, key="fb_ad")
            
            if st.button("🔍 Go to Brute Ledger", key="goto_ledger_b"):
                st.session_state.page = 'brute_ledger'
                st.rerun()
        
        # SLIDERS
        fb_cci = st.slider("CCI - Coherence & Closure", 0.0, 10.0, value=st.session_state["fb_cci"], step=0.1, key="fb_cci")
        fb_edb = st.slider("EDB - Explanatory Depth & Breadth", 0.0, 10.0, value=st.session_state["fb_edb"], step=0.1, key="fb_edb")
        fb_pf_i = st.slider("PF-Instrumental", 0.0, 10.0, value=st.session_state["fb_pfi"], step=0.1, key="fb_pfi")
        fb_pf_e = st.slider("PF-Existential", 0.0, 10.0, value=st.session_state["fb_pfe"], step=0.1, key="fb_pfe")
        fb_ar = st.slider("AR - Aesthetic Resonance", 0.0, 10.0, value=st.session_state["fb_ar"], step=0.1, key="fb_ar")
        fb_mg = st.slider("MG - Moral Generativity", 0.0, 10.0, value=st.session_state["fb_mg"], step=0.1, key="fb_mg")
        
        # PER-FRAMEWORK PRESET BUTTONS (BELOW SLIDERS - small)
        st.caption("**⚡ Quick Adjust:**")
        preset_b = st.columns(4)
        with preset_b[0]:
            if st.button("MAX", key="fb_max_btn", help="Set all to 10.0"):
                for k in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                    st.session_state[k] = 10.0
                st.rerun()
        with preset_b[1]:
            if st.button("MID", key="fb_mid_btn", help="Set all to 5.0"):
                for k in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                    st.session_state[k] = 5.0
                st.rerun()
        with preset_b[2]:
            if st.button("RESET", key="fb_reset_btn", help="Reset to CT"):
                st.session_state["fb_cci"] = CT_DEFAULT["levers"]["CCI"]
                st.session_state["fb_edb"] = CT_DEFAULT["levers"]["EDB"]
                st.session_state["fb_pfi"] = CT_DEFAULT["levers"]["PF_instrumental"]
                st.session_state["fb_pfe"] = CT_DEFAULT["levers"]["PF_existential"]
                st.session_state["fb_ar"] = CT_DEFAULT["levers"]["AR"]
                st.session_state["fb_mg"] = CT_DEFAULT["levers"]["MG"]
                st.rerun()
        with preset_b[3]:
            if st.button("MIN", key="fb_min_btn", help="Set all to 0.0"):
                for k in ["fb_cci", "fb_edb", "fb_pfi", "fb_pfe", "fb_ar", "fb_mg"]:
                    st.session_state[k] = 0.0
                st.rerun()

        fb = {
            "name": fb_name,
            "bf_i": {"axioms": fb_axioms, "debts": fb_debts},
            "levers": {"CCI": fb_cci, "EDB": fb_edb, "PF_instrumental": fb_pf_i, "PF_existential": fb_pf_e, "AR": fb_ar, "MG": fb_mg},
            "admits_limits": fb_admits
        }

    st.markdown("---")

    # CALCULATE
    ya_results, ya_levers, ya_bfi = ypa_scenario_scores(fa, cfg)
    yb_results, yb_levers, yb_bfi = ypa_scenario_scores(fb, cfg)

    # TABS
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Visual", "📋 Details", "🛡️ Guardrails", "🔄 Symmetry"])

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
            df["Flag"] = df["Delta"].apply(lambda x: "⚠️" if abs(x) > 0.3 else "✅")
            st.dataframe(df)
        with c2:
            st.markdown(f"**{fb['name']}**")
            audit = symmetry_audit(fb, cfg)
            df = pd.DataFrame(audit, columns=["Toggle", "Base", "Flip", "Delta"])
            df["Flag"] = df["Delta"].apply(lambda x: "⚠️" if abs(x) > 0.3 else "✅")
            st.dataframe(df)

    # BOTTOM: IMPORT + EXPORT
    st.markdown("---")
    st.markdown("### 📥 Import / 📤 Export")
    
    bottom_col1, bottom_col2 = st.columns(2)
    
    with bottom_col1:
        st.markdown("**📥 Import Configuration**")
        import_file_bottom = st.file_uploader("Load saved audit", type=["json"], key="import_bottom")
        if import_file_bottom:
            try:
                run = json.load(import_file_bottom)
                if "config" in run and "framework_a" in run:
                    st.success("✅ Valid profile")
                    if st.button("Apply", key="apply_bottom"):
                        apply_loaded_run(run)
                        st.rerun()
            except:
                st.error("Invalid file")
    
    with bottom_col2:
        st.markdown("**📤 Export Current Audit**")
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
            "📥 Download Audit (JSON)",
            json.dumps(export, indent=2),
            "cfa_run.json",
            "application/json",
            use_container_width=True
        )

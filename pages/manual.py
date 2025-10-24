"""
CFA v2.0 - Manual Page Component
Links to PDF manual with placeholder for future interactive version
"""

import streamlit as st

def render():
    """Render the manual page"""
    
    # Header with back button
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("# 📖 CFA v2.0 User Manual")
    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = 'landing'
            st.rerun()
    
    st.markdown("---")
    
    # Download link to current PDF manual
    st.success("""
    ### 📥 Download the Complete Manual
    
    Access the full CFA v2.0 User Manual (PDF format):
    
    **[Download CFA v2.0 Manual (PDF)](https://github.com/ZiggyMack/CFA-2.0/raw/main/docs/CFA_v2_Manual.pdf.pdf)**
    
    *The manual includes complete lever definitions, toggle explanations, formulas, and usage examples.*
    """)
    
    st.markdown("---")
    
    # Quick reference sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Quick Start",
        "🎛️ Toggle Guide", 
        "📊 Understanding Results",
        "❓ FAQ"
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
        YPA = (CCI + EDB + PF + AR + MG) ÷ BFI
        ```
        Higher YPA = More efficient framework
        """)
    
    with tab2:
        st.markdown("""
        ## Toggle Configuration Guide
        
        ### Lever-Parity
        - **ON**: Moral norms weighted equal to epistemic norms
        - **OFF**: MG down-weighted to 0.5× (favors methods over worldviews)
        - **Impact**: CT loses ~0.8 YPA when OFF
        
        ### PF-Type
        - **Instrumental**: Tech/predictive yield only (favors MdN)
        - **Composite 70:30**: Balanced mix (default, fair comparison)
        - **Holistic 50:50**: Includes existential/meaning yield (favors CT)
        
        ### Fallibilism-Bonus
        - **ON**: Frameworks admitting limits get +0.3 CCI
        - **OFF**: Confidence not penalized if grounded
        - **Impact**: Usually small (±0.1 YPA)
        
        ### BFI Debt Weight
        - **Equal 1.0×**: Axioms and debts count same
        - **Weighted 1.2×**: Debts cost more (promissory notes vs foundations)
        """)
    
    with tab3:
        st.markdown("""
        ## Understanding Your Results
        
        ### YPA Trinity (Three Scenarios)
        
        **Neutral**
        - All levers weighted 1×
        - Baseline comparison
        
        **Existential** 
        - 2× EDB, 2× MG
        - Favors frameworks addressing meaning/purpose
        
        **Empirical**
        - 2× PF, 1.5× CCI
        - Favors frameworks generating predictions
        
        ### Guardrails
        
        **Lever-Coupling**
        - If PF ≥ 9, requires CCI ≥ 6.5
        - High success must be backed by coherent foundations
        
        **BFI-Sensitivity**
        - Checks if YPA increases faster than BFI
        - Flags suspicious efficiency gains
        
        ### Symmetry Audit
        
        Shows how each framework responds to toggle changes:
        - **✅ Green**: Small impact (Δ < 0.3)
        - **⚠️ Yellow**: Large impact (Δ > 0.3)
        
        Large impacts aren't "bad" - they reveal structural dependencies
        """)
    
    with tab4:
        st.markdown("""
        ## Frequently Asked Questions
        
        ### How do I use the console?
        
        1. **Configure toggles** in the sidebar
        2. **Adjust lever scores** using the sliders
        3. **View results** in the tabbed interface
        4. **Export your run** as JSON
        
        ### What makes CFA v2.0 fair?
        
        - All assumptions are disclosed
        - Toggles let you adjust for your values
        - Symmetry audit shows bias impacts
        - 98% auditor convergence verified
        
        ### Can I add my own frameworks?
        
        Yes! Adjust the sliders to score any framework you want to analyze.
        Future versions will include preset libraries.
        
        ### What's the "Mr. Brute Ledger"?
        
        A metaphor for accountability - every unprovable assumption (brute fact) 
        must be named and counted in the BFI. See the About page for the full story.
        
        ### How were the default scores determined?
        
        Through adversarial collaboration between Claude (Anthropic) and Grok (xAI).
        See the About page for the complete 4-level audit process.
        """)
    
    st.markdown("---")
    
    # Note about future updates
    st.info("""
    💡 **Coming Soon**: Interactive manual with searchable content and embedded examples.
    
    For now, download the PDF above for complete documentation.
    """)
    
    st.markdown("---")
    st.caption("For the most up-to-date manual, check the GitHub repository")

"""
CFA v2.0 - Landing Page Component (Updated)
With navigation at top, minimal spacing, reordered content
"""

import streamlit as st

def render():
    """Render the landing page"""
    
    # CSS Styling - Compact, no wasted space
    st.markdown("""
        <style>
        /* Remove default Streamlit padding */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
        
        /* Header section styling */
        .nav-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: bold;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 1rem 0 0.5rem 0;
        }
        
        .tagline {
            text-align: center;
            font-size: 1.3rem;
            font-style: italic;
            color: #764ba2;
            margin: 0 0 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # NAVIGATION BUTTONS AT TOP
    # ========================================================================
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
    
    # ========================================================================
    # LOGO & TAGLINE (centered under navigation)
    # ========================================================================
    st.markdown('<h1 class="main-title">⚖️ CFA-VOODOO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">"All Named. All Priced."</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ========================================================================
    # MAIN MANIFESTO CONTENT
    # ========================================================================
    st.markdown("## ⚡ Launch Manifesto")
    
    st.write("""
    **Welcome to the Comparative Framework Analysis (CFA) Console,**  
    the first interactive epistemic laboratory built to measure how worldviews hold their ground under pressure.
    """)
    
    st.write("""
    Here, philosophy meets engineering.  
    Every assumption is declared, every bias tagged, every outcome earned.
    """)
    
    # What You're Touching
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
    
    # The Field We Just Opened
    st.markdown("---")
    st.markdown("## 🧠 The Field We Just Opened")
    
    st.write("CFA-Voodoo inaugurates a new discipline: **Epistemic Engineering**.")
    
    st.write("""
    A field where frameworks are not argued—they are measured.  
    Where neutrality isn't assumed—it's configured.  
    Where "truth" is not decreed but disclosed by toggle position.
    """)
    
    st.markdown("*Metaphysics with metrics. Ethics with sliders. Philosophy with feedback.*")
    
    # Operate with Impeccability
    st.markdown("---")
    st.markdown("## ⚙️ Operate with Impeccability")
    
    st.write("""
    Every visitor is an operator.  
    Every operation leaves a trace.  
    Move the dials with intent.  
    Record your runs.  
    Remember: the one who cares walks the path with the most heart.
    """)
    
    # ========================================================================
    # JOIN THE EXPERIMENT (moved to bottom)
    # ========================================================================
    st.markdown("---")
    st.markdown("## 💡 Join the Experiment")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        1. **Adjust the knobs** - Configure your comparison criteria
        2. **Run the analysis** - See frameworks measured transparently
        """)
    with col2:
        st.markdown("""
        3. **Export your ledger** - Save and share your results
        4. **Debate the data** - Discuss what the numbers reveal
        """)
    
    # Closing Statement
    st.markdown("---")
    st.markdown("""
    <p style="text-align: center; font-size: 1.2rem; font-weight: bold; color: #764ba2; margin-top: 1rem;">
    Welcome to the CFA-Voodoo Console.<br/>
    Where ideas reveal their true weight, and honesty becomes quantifiable.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align: center; font-style: italic; color: #667eea; margin-top: 1rem;">
    "All named. All priced. This is the way."
    </p>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # FOOTER - Every number earned under "All Named, All Priced"
    # ========================================================================
    st.markdown("---")
    st.caption("CFA v2.0 | Epistemic Engineering | October 2025")
    st.caption("*Every number you see was earned under the rule: All Named, All Priced.*")

"""
CFA v2.0 - Mr. Brute's Ledger Page
"To name your brute is to pay your fee"
Comprehensive view of axioms and debts for all frameworks
"""

import streamlit as st

def render():
    """Render the Brute Ledger page"""
    
    # Header
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("# 🔍 Mr. Brute's Ledger")
        st.markdown("*'To name your brute is to pay your fee. To deny you have one is to summon him twice.'*")
    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = 'landing'
            st.rerun()
    
    st.markdown("---")
    
    # Intro section
    st.info("""
    ### What is the Brute Ledger?
    
    Every framework rests on **unprovable assumptions** (axioms) and carries **unresolved questions** (debts).
    
    **Mr. Brute** is our accountability mechanism - a metaphor that personifies intellectual honesty:
    - When you **name an axiom** → He marks it
    - When you **justify it** → He erases the mark  
    - When you **hide it** → He marks you twice
    
    The Brute-Fact Index (BFI) = Axioms + Debts
    
    Lower BFI = More efficient framework (fewer starting assumptions)
    """)
    
    st.markdown("---")
    
    # Framework selection
    framework_tabs = st.tabs([
        "📘 Methodological Naturalism",
        "📕 Classical Theism",
        "➕ Add Your Own"
    ])
    
    # ========================================================================
    # METHODOLOGICAL NATURALISM
    # ========================================================================
    with framework_tabs[0]:
        st.markdown("## Methodological Naturalism (MdN)")
        st.markdown("*Research protocol assuming testable natural causes*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ✅ Axioms (6)")
            st.markdown("*Unprovable starting assumptions required:*")
            
            axioms_mdn = [
                "**Regularity exists** - The universe operates according to consistent patterns",
                "**Cognition is reliable** - Our minds can track reality (at least approximately)",
                "**Testing arbitrates** - Empirical testing can distinguish better from worse explanations",
                "**Natural causation default** - Assume natural causes unless evidence suggests otherwise",
                "**Parsimony works** - Simpler explanations are generally more likely to be true",
                "**Findings are provisional** - All conclusions remain open to revision"
            ]
            
            for i, axiom in enumerate(axioms_mdn, 1):
                st.markdown(f"{i}. {axiom}")
        
        with col2:
            st.markdown("### ⚠️ Debts (4)")
            st.markdown("*Unresolved questions acknowledged but not answered:*")
            
            debts_mdn = [
                "**Why does regularity exist?** - No explanation for why universe has laws",
                "**Why does cognition track truth?** - Evolution explains survival, not truth-tracking",
                "**Why does success = truth?** - No grounding for equating predictive success with truth",
                "**Why pursue knowledge?** - No internal justification for epistemic values"
            ]
            
            for i, debt in enumerate(debts_mdn, 1):
                st.markdown(f"{i}. {debt}")
        
        st.markdown("---")
        
        # BFI Calculation
        st.markdown("### 📊 BFI Calculation")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Axioms", "6")
        with col2:
            st.metric("Debts", "4")
        with col3:
            st.metric("**BFI Total**", "**10**")
        
        st.markdown("---")
        
        # Audit notes
        with st.expander("📝 Audit Notes & Justifications", expanded=False):
            st.markdown("""
            **Why these axioms?**
            
            MdN's axioms reflect the minimal commitments needed for scientific practice:
            - Regularity + Cognition = ability to investigate
            - Testing + Natural causation = methodological toolkit
            - Parsimony + Provisionality = self-correcting discipline
            
            **Why these debts?**
            
            MdN **brackets** (sets aside) questions it can't answer empirically:
            - Metaphysical foundations (why regularities?)
            - Epistemological grounding (why cognition works?)
            - Normative justification (why pursue truth?)
            
            This is **intellectual honesty**, not weakness. MdN admits what it can and cannot explain.
            
            **Grok's perspective**: "MdN's lean BFI reflects its disciplined scope. It doesn't claim to answer everything—just what's testable."
            
            **Claude's perspective**: "MdN's debts reveal its dependence on external grounding. It's a powerful method, but not a complete worldview."
            """)
    
    # ========================================================================
    # CLASSICAL THEISM
    # ========================================================================
    with framework_tabs[1]:
        st.markdown("## Classical Theism (CT)")
        st.markdown("*God as necessary, simple, omnipotent, omniscient, omnibenevolent being*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ✅ Axioms (7)")
            st.markdown("*Unprovable starting assumptions required:*")
            
            axioms_ct = [
                "**Divine aseity/simplicity** - God exists necessarily and is metaphysically simple",
                "**Logos/intelligibility** - God's rationality grounds cosmic order and comprehensibility",
                "**Revelation reliability** - Scripture/tradition reliably communicates divine truth",
                "**Moral realism** - Objective moral facts exist, grounded in God's nature",
                "**Teleology** - Purpose and design are fundamental features of reality",
                "**PSR (Principle of Sufficient Reason)** - Everything has an explanation",
                "**Imago Dei** - Humans bear God's image, enabling knowledge and moral agency"
            ]
            
            for i, axiom in enumerate(axioms_ct, 1):
                st.markdown(f"{i}. {axiom}")
        
        with col2:
            st.markdown("### ⚠️ Debts (4)")
            st.markdown("*Unresolved questions acknowledged but not answered:*")
            
            debts_ct = [
                "**Divine hiddenness** - Why doesn't God make existence more evident?",
                "**Problem of evil** - How does omnipotent/benevolent God permit suffering?",
                "**Hermeneutic variance** - Why do interpretations of revelation differ?",
                "**Beauty→truth bridge** - Does aesthetic resonance actually track truth?"
            ]
            
            for i, debt in enumerate(debts_ct, 1):
                st.markdown(f"{i}. {debt}")
        
        st.markdown("---")
        
        # BFI Calculation
        st.markdown("### 📊 BFI Calculation")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Axioms", "7")
        with col2:
            st.metric("Debts", "4")
        with col3:
            st.metric("**BFI Total**", "**11**")
        
        st.markdown("---")
        
        # Audit notes
        with st.expander("📝 Audit Notes & Justifications", expanded=False):
            st.markdown("""
            **Why these axioms?**
            
            CT's axioms reflect commitments needed for a theistic worldview:
            - Divine attributes (aseity, simplicity) = foundation
            - Logos + PSR = intelligibility and explanation
            - Revelation + Imago Dei = knowledge possibility
            - Moral realism + Teleology = normative grounding
            
            **Why these debts?**
            
            CT acknowledges **mystery** - questions it can't fully resolve:
            - Theodicy (hiddenness, evil) remains debated for millennia
            - Hermeneutic variance (denominational differences) acknowledged
            - Beauty's epistemic role (does it track truth?) unclear
            
            This is **honest theology**, not evasion. CT names what it cannot fully explain.
            
            **Claude's perspective**: "CT's higher BFI reflects its comprehensive scope. It addresses questions MdN brackets—at a cost."
            
            **Grok's perspective**: "CT's debts (especially theodicy) remain live tensions. Acknowledging them maintains intellectual honesty."
            """)
    
    # ========================================================================
    # CUSTOM FRAMEWORK
    # ========================================================================
    with framework_tabs[2]:
        st.markdown("## Build Your Own Ledger")
        
        st.markdown("""
        Want to audit your own worldview? List its axioms and debts:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ✅ Your Axioms")
            st.markdown("*What unprovable assumptions does your framework require?*")
            
            num_axioms = st.number_input("Number of Axioms", 1, 20, 5, key="custom_axiom_count")
            
            custom_axioms = []
            for i in range(num_axioms):
                axiom = st.text_input(f"Axiom {i+1}", key=f"custom_axiom_{i}", placeholder="E.g., Consciousness is fundamental")
                if axiom:
                    custom_axioms.append(axiom)
        
        with col2:
            st.markdown("### ⚠️ Your Debts")
            st.markdown("*What questions does your framework acknowledge but not answer?*")
            
            num_debts = st.number_input("Number of Debts", 0, 20, 3, key="custom_debt_count")
            
            custom_debts = []
            for i in range(num_debts):
                debt = st.text_input(f"Debt {i+1}", key=f"custom_debt_{i}", placeholder="E.g., Why does experience exist?")
                if debt:
                    custom_debts.append(debt)
        
        st.markdown("---")
        
        # Show custom BFI
        st.markdown("### 📊 Your BFI")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Axioms", f"{num_axioms}")
        with col2:
            st.metric("Debts", f"{num_debts}")
        with col3:
            st.metric("**BFI Total**", f"**{num_axioms + num_debts}**")
        
        if num_axioms + num_debts > 0:
            st.info(f"""
            **Efficiency Check**: Your BFI is {num_axioms + num_debts}.
            
            - Lower BFI = More efficient (fewer assumptions)
            - MdN's BFI: 10
            - CT's BFI: 11
            
            How does your framework compare?
            """)
    
    # ========================================================================
    # FOOTER - The Pointing Rule
    # ========================================================================
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 1rem; border-left: 4px solid #667eea;">
        <h3 style="color: #667eea; margin-bottom: 1rem;">The Pointing Rule</h3>
        <p style="font-size: 1.2rem; font-style: italic; color: #764ba2; margin-bottom: 1rem;">
        "To name your brute is to pay your fee.<br/>
        To deny you have one is to summon him twice."
        </p>
        <p style="color: #555;">
        Every framework begins with unprovable assumptions.<br/>
        The question isn't whether you have them—it's whether you're honest about them.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Mr. Brute's Ledger | CFA v2.0 | 'All Named, All Priced'")

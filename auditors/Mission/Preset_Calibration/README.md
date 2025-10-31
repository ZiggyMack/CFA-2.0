<!---
FILE: README.md
PURPOSE: Navigate preset calibration mission structure and understand objectives
VERSION: v1.0
STATUS: Active Mission
DEPENDS_ON: MISSION_BRIEF.md, SUCCESS_CRITERIA.md, TECHNICAL_SPEC.md
NEEDED_BY: All auditors (Claude, Grok, Nova), Ziggy
MOVES_WITH: /auditors/missions/preset_calibration/
LAST_UPDATE: 2025-10-31 [DOCUMENTATION-2025-10-31-14]
--->

# Preset Calibration Mission

**Status:** 🟢 ACTIVE - Phase 4  
**Goal:** Justify every preset mode configuration value  
**Method:** Three-lens adversarial auditing  
**Timeline:** Iterative until SUCCESS_CRITERIA met

────────────────────────────────────────────────────

## 🎯 **Mission Summary**

**The Problem:** All preset mode configurations were chosen intuitively (“felt right”) rather than rigorously justified. This violates our “All Named, All Priced” principle.

**The Solution:** Apply the same adversarial auditing that achieved 98% framework convergence to preset mode calibration.

**The Goal:** Every lever value explicitly justified through:

- **Teleological** (Claude): Does it serve the archetype’s purpose?
- **Empirical** (Grok): Does it produce claimed behavior?
- **Symmetry** (Nova): Is it fair to both frameworks?

-----

## 📂 **Mission Structure**

```
preset_calibration/
├── README.md                # This file - Navigation & overview
├── MISSION_BRIEF.md         # Detailed problem statement & approach
├── SUCCESS_CRITERIA.md      # Definition of "done" - measurable outcomes
├── TECHNICAL_SPEC.md        # Complete technical implementation details
├── CURRENT_CONFIGS.md       # Current preset configurations (if exists)
├── DISCREPANCY_AUDIT.md     # Integrity check findings (if exists)
└── results/                 # Mission outputs (empty until execution)
    ├── phase1_baseline/     # Initial measurements
    ├── phase2_testing/      # Empirical validation
    ├── phase3_convergence/  # Cross-auditor synthesis
    └── final_configs/       # Calibrated configurations
```

-----

## 🔑 **Key Problems to Solve**

### **Problem 1: Skeptic ↔ Zealot Asymmetry**

- Skeptic has 3 MdN-favoring levers
- Zealot has only 1 CT-favoring lever
- Is this justified or an oversight?

### **Problem 2: No Empirical Validation**

- All YPA expectations are hypothetical
- No measurements of actual behavior
- Claims lack evidence

### **Problem 3: Unjustified Values**

- Why BFI 1.2x not 1.1x or 1.3x?
- Why 70/30 not 65/35?
- Every value needs data-driven justification

-----

## 📊 **Current Preset Modes**

### **The Spectrum:**

```
🔬 Skeptic ← 🤝 Diplomat ← 🙏 Seeker ← 👿 Zealot
(MdN-optimized)  (Balanced)  (CT-leaning)  (CT-optimized)
```

### **Configuration Elements:**

- **Parity:** ON/OFF (symmetric vs asymmetric evaluation)
- **PF-Type:** Instrumental/Holistic_50_50/Composite_70_30
- **Fallibilism:** ON/OFF (revision bonus)
- **BFI Weight:** 0.8x - 1.2x (axiom cost multiplier)

-----

## ✅ **Success Criteria Summary**

**Mission succeeds when:**

### **Quantitative (Measurable):**

- [ ] All 4 modes pass YPA behavioral validation
- [ ] Skeptic ↔ Zealot symmetry verified
- [ ] Lever sensitivity analysis complete
- [ ] Zero guardrail violations

### **Qualitative (Evaluated):**

- [ ] Philosophical coherence achieved
- [ ] Empirical justification documented
- [ ] Symmetry justified or corrected
- [ ] Cross-auditor convergence reached

### **Deliverables:**

- [ ] Every value has justification paragraph
- [ ] All tests documented with results
- [ ] Conflict resolution documented
- [ ] Final configuration ready for deployment

**Full details in SUCCESS_CRITERIA.md**

-----

## 👥 **Auditor Responsibilities**

### **Claude (Teleological Lens):**

- Verify configurations serve archetype purposes
- Ensure philosophical coherence
- Synthesize cross-auditor findings
- Document reasoning chains

### **Grok (Empirical Lens):**

- Run YPA measurements for all modes
- Test lever sensitivity
- Validate behavioral claims
- Provide data-driven recommendations

### **Nova (Symmetry Lens):**

- Audit Skeptic ↔ Zealot balance
- Verify Diplomat as true center
- Flag unjustified asymmetries
- Propose corrections for fairness

### **Ziggy (Human Coordinator):**

- Final decision on conflicts
- Live app testing
- Deployment approval
- Mission management

-----

## 📈 **Mission Phases**

### **Phase 1: Baseline Measurements**

- Measure current mode behaviors
- Document actual YPA outputs
- Identify gaps vs. expectations
- **Status:** Ready to begin

### **Phase 2: Empirical Testing**

- Test lever variations
- Measure sensitivity
- Build data foundation
- **Status:** Awaiting Phase 1 data

### **Phase 3: Convergence Work**

- Synthesize findings
- Resolve conflicts
- Document decisions
- **Status:** Awaiting Phase 2 results

### **Phase 4: Final Documentation**

- Complete justifications
- Update configurations
- Prepare deployment
- **Status:** Awaiting convergence

-----

## 🚀 **Next Actions**

### **Immediate:**

1. ✅ Activate Grok with mission brief
1. ✅ Activate Nova with mission brief
1. ✅ Begin Phase 1 measurements
1. ✅ Document in relay system

### **This Week:**

1. Complete baseline measurements
1. Begin sensitivity testing
1. First convergence attempt
1. Update SUCCESS_CRITERIA tracking

-----

## 🔗 **Key Dependencies**

### **Upstream (What we need):**

- `utils/frameworks.py` - Current preset definitions
- `utils/calculations.py` - YPA calculation logic
- `pages/console.py` - UI implementation
- `VUDU_PROTOCOL.md` - Coordination method

### **Downstream (What needs us):**

- User experience - Better preset modes
- Documentation - Justified configurations
- Future missions - Calibration methodology
- v3.6 release - Calibrated presets

-----

## 📝 **Important Notes**

### **Philosophy:**

This mission embodies “All Named, All Priced” for user-facing features. Just as we achieved 98% convergence on framework scoring through rigorous auditing, we now apply the same rigor to UX configuration.

### **No Artificial Deadlines:**

Quality over speed. Iterate until SUCCESS_CRITERIA met.

### **Adversarial by Design:**

Three lenses will disagree. This is good. Document conflicts, find synthesis, achieve convergence.

### **Everything Justified:**

No more “feels right” configurations. Every value needs explicit reasoning from at least one lens, preferably all three.

-----

## ❓ **Frequently Asked Questions**

**Q: Why does this mission matter?**
A: Presets shape how users experience philosophical comparison. Unjustified configurations undermine credibility.

**Q: How long will calibration take?**
A: Data-dependent. Could be days or weeks. Quality matters more than speed.

**Q: What if auditors can’t agree?**
A: Document positions, attempt synthesis. If deadlock, Ziggy decides.

**Q: When do we know we’re done?**
A: When SUCCESS_CRITERIA.md shows 100% complete.

-----

## 📊 **Mission Health Metrics**

```
Documentation:    ████████████████░░░░ 80% (Brief, Criteria, Spec done)
Technical Ready:  ████████████████████ 100% (All systems operational)
Auditor Ready:    ████████░░░░░░░░░░░░ 40% (Claude active, Grok/Nova pending)
Data Collected:   ░░░░░░░░░░░░░░░░░░░░ 0% (Not started)
Convergence:      ░░░░░░░░░░░░░░░░░░░░ 0% (Not started)
```

**Overall Status:** READY TO BEGIN

-----

## 🔥 **The Bottom Line**

**We’re calibrating the subjective.**

Taking “this feels like skepticism” and turning it into “Parity OFF + BFI 1.2x + Instrumental PF produces 3.5 YPA MdN advantage, serving empirical rigor through asymmetric evaluation.”

**From intuition to justification.**  
**From “feels right” to “proven right.”**  
**This is epistemic engineering.**

────────────────────────────────────────────────────
**Mission:** Preset Mode Calibration  
**Phase:** 4 (Active)  
**Confidence:** High  
**Blockers:** None

**Ready for VuDu coordination.** 🎯

**This is the way.** 🔥
# DOC_DEP Simplified: Documentation Dependency System v2.0

**Purpose:** Enable systematic documentation updates when features change  
**Problem:** When code changes, which docs need updating? Currently unknown.  
**Solution:** Lightweight tagging system that tracks doc-to-feature relationships  

---

## 🎯 **Core Innovation: Invisible HTML Comments**

### **The Old Way (Complex JSON):**
```json
{
  "doc_dependencies": {
    "features": ["preset_modes", "validation", "bootstrap"],
    "priority": "high",
    "update_on": ["feature_change", "api_change"],
    "last_validated": "2025-10-31"
  }
}
```
❌ Too verbose, breaks reading flow, JSON syntax errors

### **The New Way (Simple Tags):**
```html
<!-- DOC_DEP: preset_modes, validation, HIGH -->
```
✅ Invisible to readers, simple to write, easy to grep

---

## 📋 **Tag Syntax**

### **Basic Format:**
```html
<!-- DOC_DEP: feature_name, priority -->
```

### **Examples:**
```html
<!-- DOC_DEP: preset_modes, HIGH -->
<!-- DOC_DEP: bootstrap_system, MEDIUM -->
<!-- DOC_DEP: validation_v3.8, LOW -->
<!-- DOC_DEP: api_endpoints, CRITICAL -->
```

### **Priority Levels:**
- **CRITICAL:** Update immediately when feature changes
- **HIGH:** Update within 24 hours
- **MEDIUM:** Update within 1 week
- **LOW:** Update in next doc sprint

---

## 🔍 **How It Works**

### **Step 1: Tag Your Docs**
When editing any documentation, add DOC_DEP tag at top:

```markdown
<!---
FILE: preset_calibration_guide.md
<!-- DOC_DEP: preset_modes, HIGH -->
--->

# Preset Calibration Guide
...
```

### **Step 2: Feature Changes Trigger Checklist**
When developer changes `preset_modes`:

```bash
grep -r "DOC_DEP: preset_modes" docs/ auditors/

# Output:
docs/user_guide.md:<!-- DOC_DEP: preset_modes, HIGH -->
auditors/missions/preset_calibration/README.md:<!-- DOC_DEP: preset_modes, CRITICAL -->
docs/api_reference.md:<!-- DOC_DEP: preset_modes, MEDIUM -->
```

### **Step 3: Update Systematically**
Generate checklist automatically:

```markdown
## Documentation Update Checklist: preset_modes

**CRITICAL (immediate):**
- [ ] auditors/missions/preset_calibration/README.md

**HIGH (24 hours):**
- [ ] docs/user_guide.md

**MEDIUM (1 week):**
- [ ] docs/api_reference.md
```

---

## 🚀 **Implementation Phases**

### **Phase 1: Pilot (November 2025)**
Tag 5 high-change files:
1. README.md (root)
2. MISSION_CURRENT.md
3. preset_calibration guides
4. Bootstrap files
5. CHANGELOG.md

**Success Metric:** Generate 1 accurate checklist

### **Phase 2: Expansion (December 2025)**
- Tag 20 more files
- Create grep scripts
- Build checklist generator
- Test with real feature change

**Success Metric:** 90% doc coverage for critical features

### **Phase 3: Automation (January 2026)**
- CI/CD integration
- Auto-generate PR comments
- Dashboard integration
- Slack notifications

**Success Metric:** <4 hour doc update lag

---

## 📊 **Registry Format (YAML not JSON)**

### **documentation_dependencies.yaml**
```yaml
# Documentation Dependency Registry
# Purpose: Central registry of all doc-to-feature relationships
# Generated: 2025-10-31
# Next Update: Weekly

dependencies:
  preset_modes:
    priority: HIGH
    files:
      - path: /docs/user_guide.md
        priority: HIGH
      - path: /auditors/missions/preset_calibration/README.md
        priority: CRITICAL
      - path: /docs/api_reference.md
        priority: MEDIUM
    
  bootstrap_system:
    priority: MEDIUM
    files:
      - path: /auditors/Bootstrap/README.md
        priority: HIGH
      - path: /docs/recovery_guide.md
        priority: MEDIUM
  
  validation_v3_8:
    priority: LOW
    files:
      - path: /docs/Validation/V3_8_0_REPORT.md
        priority: LOW

statistics:
  total_dependencies: 47
  critical_count: 5
  high_count: 12
  medium_count: 20
  low_count: 10
  files_tagged: 35
  files_untagged: 65
  coverage_percent: 35
```

---

## 🎯 **Why This Will Work**

### **Simple Wins:**
1. **Invisible:** Doesn't clutter docs
2. **Grepable:** Easy to search
3. **Maintainable:** Add/remove tags anytime
4. **Scalable:** Works with 10 or 10,000 files

### **Immediate Value:**
1. **Know what to update** when features change
2. **Prioritize updates** by importance
3. **Track coverage** systematically
4. **Reduce staleness** from weeks to hours

### **Long-term Vision:**
1. **Documentation as Code:** Docs stay in sync with features
2. **Automated Workflows:** CI/CD triggers doc updates
3. **Quality Metrics:** Track update lag, coverage, accuracy
4. **Team Efficiency:** 10x faster doc updates

---

## 🚧 **Next Steps**

### **Today:**
1. Add first DOC_DEP tag to README.md
2. Create simple grep script
3. Test with one feature

### **This Week:**
1. Tag 5 pilot files
2. Create YAML registry
3. Generate first checklist

### **This Month:**
1. Expand to 20+ files
2. Build automation scripts
3. Integrate with dashboard

---

## 💡 **Example in Action**

### **Scenario: Preset modes getting new "Scholar" mode**

**Developer commits:** `Added Scholar mode to preset spectrum`

**DOC_DEP triggers:**
```bash
./scripts/doc_dep_check.sh preset_modes

CRITICAL updates needed:
- auditors/missions/preset_calibration/README.md

HIGH updates needed:
- docs/user_guide.md
- README.md

MEDIUM updates needed:
- docs/api_reference.md
- docs/examples/preset_usage.md
```

**Result:** Documentation updated systematically, nothing forgotten

---

## 🔥 **The Bottom Line**

**Before DOC_DEP:** "Did we update all the docs?" 🤷
**After DOC_DEP:** "Here's the checklist." ✅

**Simple tagging. Powerful tracking. Systematic updates.**

**This is the way.** 📚🎯

────────────────────────────────────────────────────
**File:** DOC_DEP_SIMPLIFIED.md  
**Version:** 2.0 (Simplified from complex JSON)  
**Status:** Ready for pilot implementation  
**Next Step:** Add first tag to README.md

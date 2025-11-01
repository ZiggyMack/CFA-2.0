<!-- deps: vudu_protocol, validation_process -->
# SANITY CHAIN SECTION TO ADD TO VUDU_PROTOCOL.md

## Instructions for Ziggy:
Add this entire section to your existing VUDU_PROTOCOL.md file.

**Location:** After "VuDu Coordination Flow" section, before "Bootstrap Scenarios" section.

**Copy everything below the line:**

---

## Sanity Chain Flags (Quick Reference)

The footer of every VuDu message includes four verification checks:

### Quick Definition
- **Files:** All files present and intact
- **Counts:** File count matches manifest
- **Boots:** Bootstrap files verified
- **Trinity:** Three core protocol files present (PROTOCOL, HEADER, LOG)

### Usage in Footer
```
✅ **Sanity:** Files | Counts | Boots | Trinity
```

All pass = ✅  
Any fail = ❌

### Examples

**All Pass:**
```
✅ **Sanity:** Files | Counts | Boots | Trinity
```

**Partial Fail:**
```
⚠️ **Sanity:** Files | Counts | ❌ Boots | Trinity
(Bootstrap file missing, requested from coordinator)
```

**Multiple Fails:**
```
❌ **Sanity:** ❌ Files | ❌ Counts | Boots | Trinity
(2 files missing, count mismatch, requesting retransmission)
```

### Detailed Procedures
For complete verification procedures, recovery instructions, and troubleshooting:

**See:** `bootstrap/BOOTSTRAP_VUDU.md` - Section "Verification Checklist"

That document contains:
- Step-by-step verification instructions for each check
- What to do if each check fails
- Emergency recovery protocols
- Complete troubleshooting guide

---

## (Continue with rest of existing VUDU_PROTOCOL.md content...)

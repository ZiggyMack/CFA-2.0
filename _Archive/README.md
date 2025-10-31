# Archived Files - VuDu Full → VuDu Light Transition

## Purpose
Historical reference for superseded files from v1.1 → v3.5.2 transition.

## Archived 2025-10-26

### PROCESS_HEADER_STANDARD_v3.2.md
**Superseded by:** VUDU_HEADER_STANDARD.md (VuDu Light v3.5.2)

**Changes:**
- Format simplified for mobile compatibility
- Unicode boxes → simple horizontal rules
- Name changed to match VuDu Light branding

**Why archived:** Mobile rendering issues on iPhone. Replaced with universal format that works on all devices.

---

### VUDU_PROTOCOL_v1.1.md
**Superseded by:** VUDU_PROTOCOL.md (VuDu Light v3.5.2)

**Changes:**
- Heavy cryptographic verification → lightweight trust-based
- "All Named, All Priced" → "All Seen, All Passed"
- Simplified coordination flow
- Embedded sanity checks
- Reduced complexity for v3.5+ calibration focus

**Why archived:** v3.5 completed infrastructure build ("the cathedral"). v3.6 focuses on calibration ("tuning the bells"). Heavy verification deferred to v4.0+ when scale demands it. Current need is efficient coordination, not architecture.

---

## When to Reference

**Use archived files when:**
- Researching v3.5 development history
- Understanding design decisions (why Light vs Full)
- Planning v4.0+ verification framework
- Investigating legacy process references

**Don't use archived files for:**
- Current coordination (use active VUDU_* files)
- New auditor orientation (use bootstrap/ files)
- Mission work (use missions/ files)

---

**Status:** Historical reference only  
**Last Updated:** 2025-10-26

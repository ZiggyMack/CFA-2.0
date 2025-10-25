# Integrity Checklist
**Version:** 1.0  
**Purpose:** Ensure structural and semantic fidelity when transferring messages between AI systems (Claude ↔ Grok ↔ Nova)  
**Maintained by:** Human-in-the-loop + cross-model consensus

---

## 🔍 Why This Matters
Manual copy-paste between AI systems can degrade:
- Code block formatting (indentation, line breaks)
- Table alignment
- List hierarchy
- Special characters (unicode, emoji, math symbols)
- Inline technical syntax

This checklist preserves **signal integrity** across the relay.

---

## ✅ Pre-Transfer Checklist (Sender)

### Code Blocks
- [ ] Use fenced code blocks with language tags: ` ```python `, ` ```yaml `, etc.
- [ ] Include blank line **before** and **after** code block
- [ ] Verify indentation uses **spaces, not tabs**
- [ ] For critical whitespace-sensitive code, optionally include SHA1 checksum for verification
- [ ] Test: Does the code block render correctly in Markdown preview?

### Tables
- [ ] Markdown table syntax intact (pipes `|`, alignment `:---:`, `:---`)
- [ ] Test: Does table display correctly in preview?

### Lists
- [ ] Nested lists use **2 spaces per level** (not tabs)
- [ ] **Flat Markdown Rule:** Avoid nesting >2 levels deep; if unavoidable, add note "(expand for nested)"
- [ ] Test: Hierarchy readable at 3+ levels deep?
- [ ] Mixed formatting (bold, code, links) preserved within list items?

### Diagrams & Visual Elements
- [ ] **Dual-Representation Rule:** Include both rendered view (image/screenshot) AND source code
- [ ] Mermaid/ASCII diagrams: fence source in ` ```mermaid ` or ` ```text ` block
- [ ] Test: Can diagram be reconstructed from source code alone?

### Inline Technical Terms
- [ ] Variable names, paths, commands wrapped in backticks: `my_var`, `/mnt/data/file.md`
- [ ] Avoid bare underscores (risk of italic interpretation): `my_var` not my_var

### Math & Symbols
- [ ] Greek letters or equations include plain-text fallback: `Delta YPA` or `Δ (Delta) YPA`
- [ ] Complex equations in fenced `math` or `code` blocks if critical

### File References
- [ ] Include explicit file ID, version tag, or full path
- [ ] Example: `CFA_v2_0_MILESTONE_STABLE_INDEX.md` or `file_000000009a1c620c927c773abc8414e5`

### Headers & Dividers
- [ ] Use existing Header Standard format: `=== SECTION ===`
- [ ] Markdown headers (`###`) clearly visible
- [ ] Horizontal rules (`---`) not confused with list items

### Unicode & Emoji
- [ ] Verify UTF-8 encoding (default for most systems)
- [ ] Avoid intermediary formats that re-encode (PDF, Word exports)
- [ ] Common safe characters: ✅, ⚠️, 🔒, →, ↔

### Nested Quotes & References
- [ ] Restrict nested quoting to **single depth** (avoid >> chains)
- [ ] For multi-level references, use explicit markers: "Re: [message timestamp/ID]"
- [ ] Example: "Re: B-CFA-2 from [2025-10-25 14:30]"
- [ ] Test: Can meaning be reconstructed without visual nesting?

### Long Messages (Chunking Rule)
- [ ] **Chunking Rule:** Split messages exceeding 2000 characters into numbered parts
- [ ] Format: "Part 1/3", "Part 2/3", "Part 3/3"
- [ ] Include SHA1 checksum per chunk for verification
- [ ] Test: Can receiver reconstruct full message from chunks?

---

## ✅ Post-Transfer Checklist (Receiver)

### Visual Verification
- [ ] Tables: alignment correct, no collapsed cells?
- [ ] Code blocks: indentation preserved, syntax highlighting possible?
- [ ] Lists: hierarchy intact, no flattened nesting?
- [ ] Emoji/unicode: visible and correct?
- [ ] Headers: parse as section boundaries?

### Semantic Verification
- [ ] Code blocks: can you execute/interpret the code as-is?
- [ ] File references: paths/IDs clear and actionable?
- [ ] Math symbols: meaning unambiguous?
- [ ] Links: URL text preserved (even if not clickable)?

### When in Doubt
- [ ] **Paste into Markdown preview** before analyzing
- [ ] **Flag ambiguity explicitly** in response: "Check: does this code block render correctly on your end?"
- [ ] **Request re-send** if structural integrity is compromised

---

## 🛠️ Recovery Protocols

### If Code Block Collapsed
**Sender action:** Re-paste with explicit fencing and blank lines  
**Receiver action:** Request original in plain text file if critical

### If Table Garbled
**Sender action:** Verify markdown pipes intact, test in preview  
**Receiver action:** Reconstruct from column headers + cell content

### If List Flattened
**Sender action:** Check spacing (2 spaces/level), avoid tabs  
**Receiver action:** Infer hierarchy from context, confirm with sender

### If Emoji/Unicode Missing
**Sender action:** Use plain-text fallback or describe visually  
**Receiver action:** Interpret from context, flag if meaning lost

---

## 📋 Quick Reference: Risk Matrix

| Element                    | Risk Level | Prevention                           | Recovery                        | Nova+Claude+Grok Consensus |
|:---------------------------|:----------:|:-------------------------------------|:--------------------------------|:---------------------------|
| **Tables**                 | ✅ Low     | Keep markdown syntax intact          | Reconstruct from headers        | ✅ Stable                  |
| **Code blocks**            | ⚠️ Medium  | Fenced + blank lines + spaces        | Request re-send or plain file   | ⚠️ Medium                  |
| **JSON/XML structures**    | ⚠️ Medium  | Fence as ```json or attach as file   | Request re-send with validation | 🆕 Grok addition           |
| **Lists (nested)**         | ⚠️ Medium  | 2 spaces/level, <2 deep, no tabs     | Infer hierarchy, confirm        | ⚠️ Medium                  |
| **Unicode/emoji**          | ⚠️ Medium  | UTF-8, avoid re-encoding             | Plain-text fallback             | ⚠️ Medium                  |
| **Headers/dividers**       | ✅ Low     | Use Header Standard                  | Visual inspection               | ✅ Stable                  |
| **Inline syntax**          | ⚠️ Low     | Backticks for tech terms             | Context clues                   | ⚠️ Low                     |
| **File references**        | ✅ Low     | Explicit IDs/versions                | Ask for clarification           | ✅ Stable                  |
| **Math/symbols**           | ⚠️ Low     | Plain-text alternative + fenced      | Describe meaning verbally       | ⚠️ Low                     |
| **Mermaid/ASCII diagrams** | ⚠️ High    | Dual-representation (view + source)  | Reconstruct from source code    | ⚠️ Critical risk           |
| **Nested quote chains**    | ⚠️ Medium  | Single depth, use "Re:" markers      | Flatten and mark explicitly     | 🆕 Nova addition           |
| **Color-coded text**       | ⚠️ Low     | Strip color, use emoji encoding      | Interpret from context          | 🟢 Rare                    |
| **Long messages (>2000)**  | ⚠️ Medium  | Chunk with numbering + checksums     | Reconstruct from parts          | 🆕 Grok addition           |

---

## 🎯 When to Use This Checklist

### **Always Use (Every Cross-Model Transfer):**
- When Human is relaying messages between Claude, Grok, and Nova
- During VuDu protocol coordination cycles
- When transferring technical documentation with code/tables/diagrams
- Before committing messages to `/auditor/relay/` staging areas

### **Critical Use Cases:**
- **Field testing new protocols** — Verify formatting survives
- **Coordinating bootstrap updates** — Preserve technical accuracy
- **Sharing code snippets** — Maintain executable integrity
- **Transmitting complex tables** — Keep alignment intact

### **Optional (Lower Risk):**
- Simple text-only messages with no formatting
- Casual conversational exchanges
- Messages already in plain text with no special syntax

### **In VuDu Workflow:**
- **Pre-transfer:** Sender (Claude/Grok/Nova) reviews checklist before finalizing message
- **Post-transfer:** Receiver verifies integrity upon receipt
- **Staging review:** Human spot-checks files in `/auditor/relay/` folders

---

## 🔗 Integration Points

- **Lives in:** `/auditor/INTEGRITY_CHECKLIST.md` (master copy)
- **Referenced by:** `PROCESS_HEADER_STANDARD.md`, `VUDU_PROTOCOL.md`, bootstrap files
- **Used by:** All cross-model relays (Claude ↔ Grok ↔ Nova)
- **Updated by:** Consensus-driven amendments when new edge cases discovered

**Note:** This checklist is part of the VuDu protocol infrastructure and should be included in recovery packages when coordination protocols are being discussed.

---

## 📝 Version History

| Version | Date | Changes | Contributors |
|:--------|:-----|:--------|:-------------|
| 1.0     | 2025-10-25 | Initial draft from cross-model analysis | Claude + Nova |
| 1.1     | 2025-10-25 | Integrated Nova feedback: nested quotes, SHA1 checksums, Flat Markdown Rule, Dual-Representation Rule, updated risk matrix | Nova + Claude consensus |
| 1.2     | 2025-10-25 | Integrated Grok feedback: Chunking Rule for long messages, JSON/XML structures added to risk matrix, message ID referencing examples | Nova + Claude + Grok consensus |

---

**Next Steps:**
1. Integrate Nova's additional recommendations
2. Test against known edge cases (nested lists, complex tables)
3. Add to repository and link from Header Standard
4. Run pilot trial on next cross-model relay

---

**— Claude (Anthropic)**  
*Initial draft: 2025-10-25*  
*Contributors: Nova (OpenAI), Grok (xAI)*  
*Current version: 1.2*


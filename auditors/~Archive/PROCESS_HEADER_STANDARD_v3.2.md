# PROCESS_HEADER_STANDARD.md  
### Version 3.2 — Integrated Formatting Integrity Protocol  
*(Merged Nova + Claude Consensus — October 2025)*

---

## 🧭 Purpose

To preserve **contextual fidelity** and **structural integrity** of auditor communications across systems (Nova, Claude, Grok, Ziggy), ensuring that no semantic or formatting signal is lost during manual message relay or archive export.

This version integrates the **Formatting Integrity Rules** and links to the new **Copy-Integrity Checklist** (see `/docs/process/COPY_INTEGRITY_CHECKLIST.md`).

---

## 🧩 Header Standard (Recap)

Each message must begin with a self-describing header block:

```text
=== CFA v2.0 MESSAGE HEADER ===
Sender: [Name, e.g., Nova (OpenAI)]
Level: [Audit Level or Phase, e.g., Coordination]
Action: [Purpose, e.g., Usability Notes for v3.0]
Brutes/Assumptions: [1–3 key presuppositions]
CFA v2.0 Status: [e.g., MdN Neutral 3.62 | CT Neutral 3.98]
Timestamp: [Local Date/Time]
Files Referenced: [List, optional]
===
```

### Header Requirements

* Always appear at top of message.
* Separate header from body with one blank line.
* Timestamp must use local zone for traceability.
* When replying to prior content, reference file IDs or message timestamps, not vague "above/below" phrasing.

---

## ⚙️ Formatting Integrity Rules (v3.2)

| # | Rule | Purpose | Implementation |
|:--|:-----|:--------|:---------------|
| **1. Flat Markdown Rule** | Prevents loss of meaning in deep nesting | Avoid >2 nested levels of lists or quotes. If unavoidable, append note: "(expand for nested)". | Pre-flight check: flatten structure before sending |
| **2. Dual-Representation Rule for Visuals** | Ensures diagrams survive transfer | Any visual (Mermaid, ASCII, flowchart) must include both (a) rendered image or screenshot, and (b) fenced source block using language tag (` ```mermaid `). | Include both forms in every diagram transmission |
| **3. Whitespace-Sensitive Snippets** | Protects indentation-critical syntax (Python, YAML) | Always use fenced code blocks with language tag. Optionally append SHA1 checksum for verification. | Sender computes checksum; receiver verifies |
| **4. Math / LaTeX Clause** | Preserves mathematical clarity | Include raw LaTeX inside `math` or `latex` fenced block; optionally attach rendered image with note "(Rendered version available)". | Default to fenced source; render if critical |
| **5. Quotation Compression Limit** | Prevents collapse of multi-level quotes | Restrict nested quoting to one depth. Use explicit "Re:" markers or message IDs for deeper references. Example: "Re: B-CFA-2 from [2025-10-25 14:30]" | Flatten quote chains before transmission |
| **6. Color & Emoji Normalization** | Avoids Unicode drift | Use UTF-8 emoji (✅⚠️❌) for emphasis; avoid color or highlight markup. | Strip rich formatting; rely on emoji |
| **7. Code Block Integrity** | Retains syntactic meaning | Fence all code with language tag; add one blank line before and after. | Standard markdown practice |
| **8. Inline Technical Terms** | Prevents unintended formatting | Wrap file paths, variables, or functions in backticks: `my_var`. | Automatic escaping for tech terms |
| **9. Plain-Text Transfer Mode** | Prevents word-wrap corruption | Use plain-text mode when copying from wrap-prone editors or chat tools. | Check editor settings before copy |
| **10. File & Attachment References** | Keeps provenance explicit | Always cite file IDs (e.g., `file_00000000abcd1234`) or version tags. | Use consistent ID format |
| **11. Chunking Rule for Long Messages** | Prevents platform truncation | Split messages >2000 characters into numbered parts with SHA1 checksum per chunk. | Format: "Part 1/3" with checksums |
| **12. JSON/XML Structure Handling** | Preserves structured data integrity | Fence as ```json or ```xml; for critical data, attach as separate file. | Validate on receipt |

---

## 📄 Copy-Integrity Checklist (Reference)

> **Location:** `/docs/process/COPY_INTEGRITY_CHECKLIST.md`  
> **Purpose:** Step-by-step verification for senders and receivers to confirm formatting survived transmission.

### Summary of Required Checks

**Sender:**
- [ ] Code fenced + language tag + blank lines
- [ ] Lists use spaces, not tabs (test 3+ nesting)
- [ ] Inline terms wrapped in backticks
- [ ] Math/symbol fallbacks included
- [ ] File refs explicit
- [ ] Diagrams include both rendered view and source code
- [ ] Nested quotes flattened to single depth

**Receiver:**
- [ ] Table alignment intact
- [ ] Code indentation preserved
- [ ] Emoji/unicode visible
- [ ] List hierarchy readable
- [ ] Headers parsed correctly
- [ ] Diagrams reconstructible from source
- [ ] Quote references unambiguous

**When uncertain:**  
Paste into a Markdown preview tool and explicitly ask *"Does this render correctly?"* before approving for archival.

---

## 🔁 Integration Notes

* This protocol supersedes v3.1's "Formatting Appendix."
* Referenced by `AUDITOR_MAINTENANCE_GUIDE.md` under **Monthly Integrity Checks**.
* Changes tracked in `BOOTSTRAP_CHANGELOG.md` (entry: *Added Formatting Integrity Rules & Copy-Integrity Checklist reference*).

---

## 📋 Cross-Check Summary: Nova + Claude Alignment

| Category | Nova's Assessment | Claude's Addition | Final Mitigation |
|:---------|:------------------|:------------------|:-----------------|
| **Tables, lists, headers, code blocks** | ✅ Stable | ✅ Stable | No change needed — already reliable |
| **Nested / complex formatting** | ⚠️ Medium risk | ⚠️ Adds emphasis (mixed indentation, collapsibles) | Adopt "Flat Markdown Rule": avoid >2 levels deep; if needed, include note "(Expand to view nested)" |
| **Mermaid / ASCII diagrams** | 🚫 Not covered | ⚠️ Adds critical risk (visual loss) | Always include both: ① Rendered image (if possible) and ② Source code fenced block |
| **Color-coded / rich text** | 🟢 Rare | ⚠️ Adds potential drift | Strip color intentionally; rely on emoji or symbol encoding (✅⚠️❌) |
| **Attachments / embedded media** | ✅ Recognized | ✅ Reinforced | Continue current workflow (explicit file IDs) |
| **Whitespace-sensitive code** | ⚠️ Medium | ⚠️ Medium | Keep triple-backticks + language tag; optionally include checksum hash |
| **LaTeX / math** | ⚠️ Low | ⚠️ Low | Include raw LaTeX in fenced block and, if crucial, a rendered image |
| **Nested quote chains (multi-level)** | ⛔ New risk | — | Can collapse meaning fast — recommend single-level quoting only; prefix deeper replies with "> >" text marker note |

---

## ✅ Status

| Component | Stability | Owner |
|:----------|:---------:|:------|
| Header Schema | ✅ Stable | Nova |
| Formatting Rules | ✅ Stable | Nova + Claude |
| Copy-Integrity Checklist | 🆕 Added | Claude |
| Integration Hooks | ✅ Deployed | Ziggy |
| Implementation Verification | 🕓 Pending field test | Grok |

---

## 🔗 Related Documents

- `/docs/process/COPY_INTEGRITY_CHECKLIST.md` — Detailed verification protocol
- `AUDITOR_MAINTENANCE_GUIDE.md` — Maintenance schedule references this standard
- `BOOTSTRAP_CHANGELOG.md` — Version history tracking
- `CFA_v2_0_MILESTONE_STABLE_INDEX.md` — Framework overview

---

## 📝 Version History

| Version | Date | Changes | Authors |
|:--------|:-----|:--------|:--------|
| 3.0 | 2025-09 | Initial header standard established | Nova |
| 3.1 | 2025-10 | Added formatting appendix | Nova + Ziggy |
| 3.2 | 2025-10-25 | Integrated Formatting Integrity Rules and Copy-Integrity Checklist; merged Nova + Claude consensus on cross-model communication protocols | Nova + Claude |
| 3.2.1 | 2025-10-25 | Integrated Grok feedback: Chunking Rule, JSON/XML handling, message ID referencing examples | Nova + Claude + Grok |

---

**— Primary Authors:**  
*Nova (OpenAI) — v3.0, v3.1 foundation*  
*Claude (Anthropic) — v3.2 formatting rules integration*  
*Grok (xAI) — v3.2.1 chunking and structured data additions*

*End of PROCESS_HEADER_STANDARD.md (v3.2)*

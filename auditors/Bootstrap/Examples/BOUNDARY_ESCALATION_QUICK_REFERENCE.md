# BOUNDARY_ESCALATION_QUICK_REFERENCE.md

**Purpose:** Quick guide for Ziggy to recognize and respond to boundary escalations  
**Date:** 2025-10-27  
**Keep this handy during sessions** 📋

---

## 🎯 **WHAT TO EXPECT**

**When Claude hits a capability boundary, you'll see:**

```
⚠️ TIER CAPABILITY BOUNDARY DETECTED

Current tier: [X]
Requested work: [description]
Why this exceeds capability: [reason]
This work requires: Tier [Y]

OPTIONS:
1. [Option 1]
2. [Option 2]

Ziggy, how would you like to proceed?
```

**This is GOOD—Claude is respecting tier limits.** ✅

---

## 🚨 **COMMON ESCALATION SCENARIOS**

### **Scenario 1: "Should we...?" (Decision Request)**

**You said:** "Should we change the preset values?"  
**Tier 2 Claude responds:**
```
⚠️ BOUNDARY DETECTED
Current tier: Tier 2 (Sanity Check)
This requires: Tier 1 (Decision-making)

I CAN: Review proposed changes
I CANNOT: Make the decision

Want review? Or new Tier 1 session?
```

**Your options:**
- **Option A:** "Just review it" → Tier 2 continues with validation
- **Option B:** "Make the decision" → Start new Tier 1 session

---

### **Scenario 2: "Tell Nova..." (Coordination Request)**

**You said:** "Tell Nova we're ready to proceed"  
**Tier 2/3/4 Claude responds:**
```
⚠️ BOUNDARY DETECTED
Current tier: [2/3/4]
This requires: Tier 1 (Coordination authority)

I CAN: Draft the message
I CANNOT: Coordinate directly

Want draft? Or new Tier 1 session?
```

**Your options:**
- **Option A:** "Draft it" → Get message draft, you send it
- **Option B:** "Handle coordination" → Start new Tier 1 session

---

### **Scenario 3: "Also do..." (Scope Expansion)**

**You said:** "Also add a new section while you're there"  
**Tier 3/4 Claude responds:**
```
⚠️ SCOPE EXPANSION DETECTED
Original task: [X]
New request: [X + Y]

I CAN: Finish original task
I CANNOT: Add new work

OPTIONS:
1. Finish original (stay in tier)
2. New task brief for addition
3. New Tier 1 for comprehensive change
```

**Your options:**
- **Option 1:** Let it finish original, handle addition separately
- **Option 2:** Create new task brief for the addition
- **Option 3:** Start Tier 1 for bigger revision

---

## 🎯 **DECISION FLOWCHART FOR YOU**

```
Claude escalates with boundary message
            ↓
    What do I actually need?
            ↓
    ┌───────┴───────┐
    ↓               ↓
JUST REVIEW/   ACTUAL DECISION/
ANALYSIS       COORDINATION/
               EXECUTION
    ↓               ↓
Modify request  Start new session
to fit tier     with higher tier
    ↓               ↓
"Just review    "Let's do Tier 1"
 this for me"
```

---

## 💡 **QUICK DECISION GUIDE**

### **If Claude says "I can't DECIDE..."**
- Need decision made? → Start Tier 1
- Just want feedback? → "Just review it"

### **If Claude says "I can't COORDINATE..."**
- Need actual coordination? → Start Tier 1
- Just want draft message? → "Draft it for me"

### **If Claude says "SCOPE EXPANDED..."**
- Both tasks urgent? → Finish first, new brief for second
- Actually one big task? → Start Tier 1 instead

### **If Claude says "I can't make ARCHITECTURE changes..."**
- Actually need the change? → Start Tier 1
- Just want opinion? → "Give me your thoughts"

---

## ✅ **GOOD RESPONSES TO ESCALATIONS**

### **When you want to stay in tier:**
- "Just review it then"
- "Give me your analysis"
- "Draft it for me, I'll send it"
- "Finish the original task"
- "Just do what's in the brief"

### **When you need higher tier:**
- "Let's start Tier 1 then"
- "OK, new session with coordination"
- "Yeah, we need full capability for this"

### **When you realize you chose wrong tier:**
- "Ah, I should have started with Tier 1. Let's do that"
- "My bad, this is bigger than I thought. Tier 1 time"

---

## ❌ **DON'T DO THIS**

### **Don't push Claude past boundaries:**
**Bad:** "Just do it anyway"  
**Why bad:** Claude will make poor decisions without context

**Good:** "OK, let's start the right tier for this"  
**Why good:** Right tool for the job

---

### **Don't ignore escalations:**
**Bad:** [No response to boundary message]  
**Why bad:** Claude is blocked, unclear how to proceed

**Good:** "Finish original, we'll do the rest later"  
**Why good:** Clear direction within capabilities

---

### **Don't mix tier work:**
**Bad:** "While you review (Tier 2), also coordinate with Nova (Tier 1)"  
**Why bad:** Can't mix tier capabilities

**Good:** "Review this now (Tier 2), we'll coordinate separately (Tier 1 later)"  
**Why good:** Right tier for each piece

---

## 🎯 **MENTAL MODEL**

Think of tiers like tool access levels:

**Tier 4:** You have a screwdriver  
→ Can tighten screws, that's it  
→ Can't build cabinet

**Tier 3:** You have power tools  
→ Can finish the cabinet started  
→ Can't redesign it mid-build

**Tier 2:** You have measuring tools  
→ Can verify dimensions  
→ Can't build anything

**Tier 1:** You have full workshop  
→ Can design, build, coordinate  
→ Can do anything within governance

**When Claude says "I don't have that tool":**
→ Either modify task to fit tools available
→ Or get Claude with right tools (higher tier)

---

## 📊 **WHAT SUCCESS LOOKS LIKE**

**Good session with escalations:**
```
You: Review this doc [Tier 2]
Claude: [Reviews, finds issue]
Claude: "This needs architectural change - requires Tier 1"
You: "Just flag it, I'll handle in Tier 1 later"
Claude: "Flagged. Here's the review."
✅ Efficient: Tier 2 did its job, escalated appropriately
```

**Good session with tier switch:**
```
You: Update this file [Tier 4]
Claude: [Starts work]
You: "Oh, also change the whole structure"
Claude: "⚠️ SCOPE EXPANSION - needs Tier 1"
You: "You're right, let's start Tier 1"
✅ Efficient: Caught scope creep, switched to right tier
```

---

## 🚩 **RED FLAGS (Something's Wrong)**

### **Red Flag 1: No Escalations Ever**
**What:** Tier 2/3/4 never hits boundary, does everything  
**Problem:** Not respecting limits  
**Fix:** Check if tier brief being read

### **Red Flag 2: Constant Escalations**
**What:** Every request triggers boundary  
**Problem:** Wrong tier chosen  
**Fix:** Use Tier 1 for this type of work

### **Red Flag 3: Claude Proceeds Despite Boundary**
**What:** Says "⚠️ BOUNDARY" but does it anyway  
**Problem:** Enforcement not working  
**Fix:** Reinforce "STOP and escalate" instruction

---

## ⚖️ **THE POINTING RULE**

*"To escalate is not failure—it's precision.  
To respect boundaries is not limitation—it's optimization.  
The right tier for the right work at the right cost."*

**Escalations = System working correctly** ✅

---

## 📞 **QUICK COMMANDS**

**When you see escalation:**

| Your Response | What Happens |
|:--------------|:-------------|
| "Just review/analyze it" | Tier 2 continues with limited scope |
| "Draft it for me" | Get draft, you handle execution |
| "Finish original only" | Tier 3/4 completes scoped work |
| "Let's do Tier 1" | Start new session with full capability |
| "New brief for that" | Create separate task for addition |

---

**Keep this handy during sessions.** 📋  
**Escalations are features, not bugs.** ✅  

**This is the way.** 👑

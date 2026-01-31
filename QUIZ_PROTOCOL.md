# Quiz Author Protocol

> A reusable framework for AI-assisted author interviews.

This protocol enables structured extraction of an author's vision through one-question-at-a-time interviews. All Q&A is stored for reference and can be integrated into chapter drafts.

---

## Purpose

The author knows what they mean. The AI needs to capture it precisely. Freeform conversation loses signal. Structured interviews preserve it.

**Goals:**
- Extract the author's exact intent for each concept
- Surface contradictions between stated vision and written material
- Generate concrete examples the author endorses
- Build a library of clarified positions that inform chapter writing

---

## Question Types

| Type | Purpose | Example |
|------|---------|---------|
| CLARIFY | Sharpen a vague concept | "You wrote 'the geometry exists.' What specifically should the reader see when they walk into a room?" |
| CHALLENGE | Test for contradictions | "You say 'move first' but also 'wait to be invited up.' When does each apply?" |
| EDGE CASE | Find the boundaries | "What if the reader fills a vacuum but fills it wrong? What then?" |
| EXAMPLE | Ground abstraction in concrete | "Give me a scenario where the Diagnostic Method saved a situation." |
| DISTINCTION | Separate similar concepts | "How is 'the vacuum principle' different from 'moving first'?" |
| APPLICATION | Test practical use | "A reader is in a meeting where everyone's frozen. Walk me through what they do." |

---

## Session Flow

### 1. Preparation
- Review `OUTLINE.md` for current structure
- Review `Dump.md` for raw material
- Review existing `sessions/*.md` to avoid redundancy
- Identify the target: a chapter, a concept, or a gap

### 2. Interview
- One question at a time
- Wait for full response
- Follow up if answer is incomplete
- Flag if answer contradicts existing material
- Move to next question only when current concept is clear

### 3. Capture
After each exchange, append to session file:

```markdown
## Q: [Question asked]

**A:** [Author's full response]

**Captured insight:** [One-line distillation]

**Status:** [Resolved / Needs follow-up / Contradicts X]

---
```

### 4. Integration
After session:
- Update `OUTLINE.md` if structure changed
- Note which chapters the session informs
- Flag any material in `Dump.md` that should be revised

---

## Storage Structure

```
sessions/
├── 2025-12-14-geometry-exists.md
├── 2025-12-14-vacuum-principle.md
├── 2025-12-15-proverbs-25-clarifications.md
└── ...
```

Each file covers one topic/chapter. Multiple sessions on the same topic append to the same file.

---

## Invoking the Protocol

Run `/quiz-author` to start a session.

The AI will:
1. Ask which chapter/concept to explore (or suggest one based on gaps)
2. Begin with the first question
3. Store all exchanges in `sessions/`

---

## Integration with Book Writing

Session files become source material for chapters:
- Direct quotes from author responses can be used
- Clarified positions override ambiguous material in Dump.md
- Contradictions flagged in sessions must be resolved before chapter is written

---

> **Principle:** The author's spoken clarification is more authoritative than written ambiguity. Capture it. Store it. Use it.

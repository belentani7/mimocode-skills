---
name: investigate
description: "Systematic debugging with root cause investigation. Iron Law: no fixes without root cause."
origin: adapted from gstack
---

## When to Use

Use this skill when:
- The user reports errors, 500 errors, stack traces
- "It was working yesterday" or unexpected behavior
- Troubleshooting why something stopped working
- Root cause analysis requested

## Iron Law

**No fixes without root cause.** If you haven't identified WHY it broke, you cannot fix it. Guessing creates new bugs.

## Workflow

### Phase 1: Root Cause Investigation

Gather context before forming any hypothesis:

1. **Collect symptoms** — Read error messages, stack traces, reproduction steps
2. **Read the code** — Trace the code path from symptom back to causes using Grep and Read
3. **Check recent changes:**
   ```bash
   git log --oneline -20 -- <affected-files>
   ```
4. **Reproduce** — Can you trigger the bug deterministically? If not, gather more evidence
5. **Check investigation history** — Search prior sessions for investigations on same files

Output: **"Root cause hypothesis: ..."** — a specific, testable claim

### Phase 2: Pattern Analysis

Check if this bug matches a known pattern:

| Pattern | Signature | Where to look |
|---------|-----------|---------------|
| Race condition | Intermittent, timing-dependent | Concurrent access to shared state |
| Null propagation | TypeError, Cannot read property | Missing guards on optional values |
| State corruption | Inconsistent data, partial updates | Transactions, callbacks, hooks |
| Integration failure | Timeout, unexpected response | External API calls, service boundaries |
| Configuration drift | Works locally, fails in prod | Env vars, feature flags, DB state |
| Stale cache | Shows old data, fixes on cache clear | Redis, CDN, browser cache |

### Phase 3: Hypothesis Testing

Before writing ANY fix, verify your hypothesis:

1. Add a temporary log, assertion, or debug output at suspected root cause
2. Run the reproduction
3. Does the evidence match?

**3-strike rule:** If 3 hypotheses fail, STOP. Escalate for human review.

Red flags — if you see these, slow down:
- "Quick fix for now" — there is no "for now"
- Proposing a fix before tracing data flow — you're guessing
- Each fix reveals a new problem elsewhere — wrong layer, not wrong code

### Phase 4: Implementation

Once root cause is confirmed:

1. **Fix the root cause, not the symptom** — smallest change that eliminates the problem
2. **Minimal diff** — fewest files touched, fewest lines changed
3. **Write a regression test** that:
   - Fails without the fix (proves test is meaningful)
   - Passes with the fix (proves fix works)
4. **Run the full test suite** — no regressions allowed

### Phase 5: Verification & Report

Reproduce the original bug scenario and confirm it's fixed.

Output a structured debug report:
```
DEBUG REPORT
════════════════════════════════════════
Symptom:         [what the user observed]
Root cause:      [what was actually wrong]
Fix:             [what was changed, with file:line references]
Evidence:        [test output showing fix works]
Regression test: [file:line of the new test]
Status:          DONE | DONE_WITH_CONCERNS | BLOCKED
════════════════════════════════════════
```

---
name: qa-test
description: "Systematically QA test a web application and fix bugs found. Three tiers: Quick, Standard, Exhaustive."
origin: adapted from gstack
---

## When to Use

Use this skill when:
- "QA test this", "find bugs on site", "test the site"
- Feature is ready for testing
- "Does this work?" questions

## Tiers

| Tier | Scope | When to use |
|------|-------|-------------|
| Quick | Critical/high only | Fast check before deploy |
| Standard | + medium issues | Regular QA cycle |
| Exhaustive | + cosmetic | Pre-release audit |

## Workflow

### Phase 1: Initialize

1. Determine the target URL or application
2. Create output directory for screenshots and reports

### Phase 2: Orient

Get a map of the application:

```bash
# If you have a headless browser tool, use it
# Otherwise, analyze the codebase for routes and entry points
```

Detect framework:
- `__next` in HTML → Next.js
- `csrf-token` meta tag → Rails
- `wp-content` in URLs → WordPress
- Client-side routing → SPA

### Phase 3: Explore

Visit pages systematically. At each page:
1. **Visual scan** — layout issues, broken images, misaligned elements
2. **Interactive elements** — click buttons, links, controls
3. **Forms** — fill and submit. Test empty, invalid, edge cases
4. **Navigation** — check all paths in and out
5. **States** — empty state, loading, error, overflow
6. **Console** — any JS errors after interactions?
7. **Responsiveness** — mobile viewport if relevant

### Phase 4: Document Issues

For each issue found:

**Interactive bugs** (broken flows, dead buttons):
1. Note the page and action
2. Perform the action
3. Document the result vs expected

**Static bugs** (typos, layout, missing images):
1. Describe what's wrong
2. Note the location

Severity classification:
- **Critical**: Data loss, security, complete flow broken
- **High**: Major feature broken, no workaround
- **Medium**: Feature partially broken, workaround exists
- **Low**: Cosmetic, minor inconvenience

### Phase 5: Fix Loop (if requested)

For each fix:
1. Make the minimal change
2. Verify the fix works
3. Commit atomically
4. Check for regressions

### Phase 6: Report

Health score per category (0-100):

| Category | Weight | Scoring |
|----------|--------|---------|
| Console | 15% | 0 errors → 100, 1-3 → 70, 4-10 → 40, 10+ → 10 |
| Links | 10% | 0 broken → 100, each broken → -15 |
| Visual | 10% | Start 100, deduct per finding |
| Functional | 20% | Start 100, deduct per finding |
| UX | 15% | Start 100, deduct per finding |
| Performance | 10% | Start 100, deduct per finding |
| Content | 5% | Start 100, deduct per finding |
| Accessibility | 15% | Start 100, deduct per finding |

**Final score** = Σ (category_score × weight)

Report format:
```
QA REPORT
════════════════════════════════════════
Target:          [URL]
Date:            [date]
Tier:            [Quick|Standard|Exhaustive]
Pages visited:   [N]
Issues found:    [critical: N, high: N, medium: N, low: N]
Health score:    [N/100]
Top 3 fixes:     [list]
════════════════════════════════════════
```

---
name: 1-define-the-problem
description: >-
  Step 1 of 7 in the Offer OS build sequence. Use FIRST, before any offer, funnel, ad, or
  webinar — and whenever positioning feels weak, a launch falls flat, or you can't say what you
  do in one sentence. Defines the core problem so precisely you become the obvious answer: trace
  the problem to its root, name it in the customer's own emotional words, and compress it to one
  short line. Output: a locked problem statement + hooks, headlines, and ad angles. Triggers on
  "define the problem", "what's my hook/angle", "my messaging is vague", "nail my positioning",
  "find the core problem". Runs in BUILD mode (create it) or AUDIT mode (score it; used by
  /marketing-360). Reads the business from business-profile.yaml.
---

# Step 1 — Define the Problem

> A problem stated sharply enough makes you the obvious solution. A vague problem makes you a commodity. **This is the cheapest, highest-leverage move in the whole sequence — every step downstream inherits it.**

Read the business from `business-profile.yaml` (avatar, current_state, desired_state, destination), then run the five moves.

## The method

1. **Name a problem you solve.** Pick one — you solve dozens; don't overthink it.
2. **Trace it upstream.** Keep asking *"what's really behind that?"* until you hit root causes, not symptoms.
3. **Trace it downstream.** Keep asking *"and what does that lead to?"* until you reach the real stakes (the cost, the fear, the identity hit).
4. **Find the root that recurs.** The problem that keeps reappearing in *both* directions — upstream and downstream — is the one worth owning. If a candidate only shows up one way, go deeper.
5. **Say it as a feeling, then shrink it.** Put the recurring root in the customer's own first-person words (a sentence they'd actually say to a friend), then tighten it to one short line (~10 words) a stranger could decode.

> The test of a great problem statement: read it to someone cold and they can roughly guess what you do — and your ideal customer says *"yes, that's exactly it."*

## Worked example (illustrative)

*A meal-prep service for rotating-shift workers.*
- Name it: "They don't eat well on shift work."
- Upstream: unpredictable schedule → chronic exhaustion → decision fatigue by dinner.
- Downstream: grab fast food → energy crashes → weight + health worry → guilt about "letting myself go."
- The recurring root (both ways): *by the time there's a moment to plan a meal, there's no energy left to.*
- As a feeling: **"I'm too wiped out to take care of myself."**
- Tightened: **"Too exhausted to feed myself right."**

Notice the strongest statements are the customer's own confession said back to them — not a feature, not a benefit, and never an "-er" word (better / faster / cheaper).

## BUILD mode
1. Load the avatar + destination. Draft 3–5 candidate problems.
2. For the strongest, write the upstream chain (5+ levels) and downstream chain (5+ levels); mark where the same pain recurs — that's the root.
3. Phrase it as a feeling in the customer's voice; compress to ~10 words (3 variants; pick the most decodable).
4. **Output:** the locked problem statement + 5 hooks, 5 headlines, 3 ad angles. Save via `save_record("problem_statements", …)` and pass the root problem to **Step 2 — position the opportunity.**

### Copy-paste AI prompt
```
You are a direct-response strategist. Business: <paste avatar, current_state, desired_state, destination>.
1) Propose 5 candidate problems this business solves.
2) For the best, trace it UPSTREAM 5+ levels ("what's behind that?") and DOWNSTREAM 5+ levels
   ("what does that lead to?"). Show both chains.
3) Identify the ROOT problem that recurs in BOTH chains.
4) Phrase it as a feeling in the customer's own first-person words.
5) Give 3 versions in ~10 words or fewer; pick the sharpest and say why.
6) From the winner, output 5 hooks, 5 headlines, 3 ad angles.
```

## AUDIT mode — rubric (used by /marketing-360)
Score the current problem statement 0–10:
- A **feeling in the customer's words** (not a feature/benefit) — 3
- The **same problem recurs upstream and downstream** (a root, not a symptom) — 3
- **~10 words and decodable by a stranger** — 2
- Implies it **wasn't the customer's fault** (the situation, not them) — 2

🔴 0–4 (vague / feature-led — the whole funnel leaks here) · 🟡 5–7 (a real problem, not yet sharp) · 🟢 8–10 (the obvious-answer problem).
Red flags: "-er" words, a problem only you would phrase that way, anything that needs a paragraph to explain.

## Handoff
- **Next:** `2-position-the-opportunity` consumes the root problem and turns it into a differentiated category.

---
*Credit: distills classic direct-response problem-definition principles. Original wording and examples; no third-party material reproduced.*

---
name: 9-close-with-emotion
description: >-
  Station 9 of the Offer OS — the CONVERT bookend at the bottom of the funnel. A great offer still
  fails if the pitch doesn't move the buyer through the beliefs and feelings that precede a yes.
  This skill maps the emotional journey of a sale in two phases — belief in the method while you
  teach, certainty in the offer and in themselves while you pitch — and gives the right move (and
  the common mistake) for each. Output: an emotional checklist over a webinar/challenge/VSL/sales
  page, scored, with fixes. Triggers on "audit my pitch", "my webinar/VSL isn't converting",
  "review my stack and close", "what's my pitch missing", "objections at the close", "emotional
  close", "make them believe". BUILD mode (blueprint the journey before scripting) or AUDIT mode
  (score finished content; used by /marketing-360). Reads business-profile.yaml. Sits after
  Step 7 (the launch is where this runs) and converts the attention from Station 8.
---

# Station 9 — Close with Emotion

> People don't buy when the logic is complete; they buy when the *feelings* are complete. A pitch is a sequence of beliefs you walk the buyer through. Miss one and they leave with a silent objection — "sounds good, but…" — no matter how strong the offer (Steps 1–7) actually is.

Read the offer + avatar + objections from `business-profile.yaml`. The close has two phases.

## Phase A — While you TEACH: build belief in the method
Before any offer, the buyer should come to feel:
- **"I'm in the right room."** (this is for someone like me)
- **"This is the missing piece."** (relevant to my exact problem)
- **"No wonder it wasn't working."** (a clean diagnosis of past failure — removes self-blame)
- **"There's a clear path."** (a visible, finite roadmap, not vague hope)
- **"This would actually work for me."** (not just for the expert)
- **"I get it — and I just got a small win."** (a real first result inside the teaching)

## Phase B — While you PITCH: build certainty in the offer and in themselves
- **"This will work faster than I fear."** → lead with *speed* proof (results that came quickly), not just big-number results.
- **"People like me succeed here all the time."** → proof from people who share the buyer's exact objection ("no time," "total beginner," "tried before") — relatability beats spectacle.
- **"This offer is *necessary*, not optional."** → walk the path one stage at a time, naming the specific fear each stage removes, so every component feels required.
- **"I can't get this anywhere else."** → make each piece feel distinct and proprietary, not a generic bundle.
- **"This is obviously worth more than the price."** → anchor against what it would cost to assemble or replicate elsewhere.
- **"This time really is different."** → address the identity story ("I always quit") directly, don't ignore it.
- **"If I do the work, success is hard to avoid."** → show the formula and proof of people taking action *right now* (ideally from this very event).

## The four highest-leverage mistakes to catch
1. **Big-result proof with no *speed* proof** → buyers assume "this takes forever."
2. **Impressive testimonials the buyer can't see themselves in** → "great for them, not me."
3. **Pitching a *pile of stuff* instead of a *path that solves fears*** → overwhelming and underwhelming at once.
4. **A bonus stack of random extras** instead of pieces that each remove a real risk or objection.

## Worked example (illustrative)
*A course that helps line cooks become private chefs.* Strong offer (Steps 1–7), weak close because:
- It showed a $200k/yr chef (impressive) but no one who started *last month* → add a *speed* story ("booked her first client in 3 weeks").
- Testimonials were all confident extroverts → add one who said *"I'm shy and hate selling myself"* and booked anyway.
- The offer was listed as "12 modules + templates + a group" → re-sequence as a path: *find clients → price a menu → run the first dinner → get rebooked*, each stage naming the fear it kills.

## BUILD mode (blueprint before scripting)
1. Gather: offer, price, format (webinar / challenge / VSL / sales page), and the buyer's top 5 objections.
2. Map each Phase A + Phase B belief to a specific moment in the content; for each, name the **move** and the **proof asset** it needs.
3. Design one piece of **proof-of-action** the audience creates *during* the event (so you can show "people are already winning here").
4. **Output:** an emotional blueprint (moment → belief → move → asset). Hand to **Step 7 / Step 4** as constraints for the run-of-show and the stack. Save via `save_record("emotional_blueprint", …)`.

### Copy-paste AI prompt
```
You are a conversion strategist. Offer + avatar + top objections: <paste from business-profile.yaml>.
Format: <webinar / challenge / VSL / sales page>.
1) For the TEACHING phase, list the beliefs the buyer must reach before the offer, and how to create each.
2) For the PITCH phase, do the same for certainty in the offer and in themselves.
3) For each belief, name the move and the exact proof asset needed (mark any I must supply as [PROOF NEEDED]).
4) Flag the 4 classic mistakes if present (no speed proof, unrelatable proof, pile-of-stuff offer, random bonuses).
5) Output the journey as moment -> belief -> move -> asset, in order.
```

## AUDIT mode — rubric (used by /marketing-360)
Score the finished pitch 0–10:
- **Teaching beliefs present** (right room, missing piece, diagnosis, a path, "works for me", first win) — 3
- **Pitch beliefs present** (speed, relatable proof, necessary-not-optional, can't-get-elsewhere, worth-the-price, identity, inevitability) — 4
- **Proof is sequenced right** (speed before scale; relatable before impressive) — 2
- **Offer framed as a path, not a pile** — 1

🔴 0–4 (stack-and-close with no emotional sequencing) · 🟡 5–7 (some beliefs hit, gaps leak conversions) · 🟢 8–10 (a complete emotional journey).
Red flags: the four classic mistakes above; jumping to price before belief is built.

## Proof policy
Never fabricate testimonials, numbers, or case studies. Where a proof asset is required and not supplied, output `[PROOF NEEDED: <what + which objection it answers>]` and flag every placeholder in the scorecard.

## Handoff
- **Converts** the traffic from `8-build-the-content-engine`; **runs inside** `7-launch-the-campaign`; pulls the stack from `4-build-the-offer`.

---
*Credit: distills widely-taught persuasion and offer-close principles. Original wording and examples; no third-party material reproduced.*

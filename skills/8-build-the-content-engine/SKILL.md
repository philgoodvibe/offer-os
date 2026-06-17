---
name: 8-build-the-content-engine
description: >-
  Station 8 of the Offer OS — the ATTRACT bookend that feeds the whole funnel. Builds an organic
  content engine that reliably manufactures attention instead of posting and praying: pick topics
  on the customer's problem path, put a real human on screen, script so the viewer knows exactly
  what to do, and iterate on one honest attention metric. Output: a topic slate, scripted hooks,
  and a test-and-scale loop. Triggers on "content strategy", "organic growth", "grow my following",
  "my reels/shorts/posts aren't working", "what should I post", "why are my views low", "should I
  batch content", "go viral". BUILD mode (design the engine) or AUDIT mode (score it; used by
  /marketing-360). Reads the business from business-profile.yaml. Pairs with Step 1 (topics come
  off the problem path) and Step 5 (every post points at the funnel).
---

# Station 8 — Build the Content Engine

> Attention is the raw material the rest of the funnel runs on. Most accounts treat content as luck; treat it as an **engine** — inputs, an output metric, and a loop that compounds. The 7-step offer build sits *downstream* of this: no traffic in, nothing to convert.

Read the business from `business-profile.yaml` (avatar, problem, destination), pull the locked problem from **Step 1**, and run the engine's three gears.

## The one-line diagnostic

Every piece of content does exactly one job: **grab attention, build belief, or invite action.** When an account isn't growing, find which of the three is missing — usually it's *attention* (no reason to stop scrolling) or *action* (nothing the viewer can actually do) — and fix that one thing instead of remaking everything.

## The three gears

**Gear 1 — Make the right *type* of content.** Two non-negotiables:
- **On the problem path.** The topic is a real problem your buyer already feels — the same problems your offer solves (straight from Step 1). Content that's popular but unrelated to the offer buys views you can't convert; content only an insider would search for buys silence.
- **A human on screen.** A face, a voice, a point of view, visible expertise. People follow people. Faceless, generic content has nothing to attach to.

**Gear 2 — Say it so it's *usable*, not just *interesting*.** The test: *after watching, does the viewer know exactly what to do?*
| ❌ Idea-only | ✅ Usable |
|---|---|
| An abstract fact with no next step | A specific action the viewer can take today and get a result |

Two reliable formats: **"Do this"** (you instruct) or **"I did this"** (you show your own result). Build each piece in four moves:
1. **Topic** — one problem off the problem path.
2. **The promised result** — finish this sentence first: *"After watching, they'll do ___ and get ___."*
3. **Make it stick** — give it a reason to be *saved* (a moment they'll come back for) and *shared* (who sends it to whom).
4. **Simplify hard** — if a beginner couldn't follow it, cut the jargon. The simplest version usually wins.

**Gear 3 — Run the loop (iterate on data).**
- Judge on **one honest attention metric** (e.g. views / reach) — above your own average means *do more of this*; below means *don't*. Vanity counts (likes on a tiny post) don't drive the decision.
- On your above-average pieces, test **one variable at a time** — topic, hook, or format — so you learn what actually moved it. The hook (first 1–3 seconds / first line) is usually the highest-leverage single change.
- **Goal:** your old *best* piece becomes your new *average* piece.
- **Don't mass-produce early.** Batching locks in a format before the data has spoken. Earn batch size with results: little proof → make a couple at a time; strong, stable averages → batch freely.

## Worked example (illustrative)

*A bookkeeping service for freelancers.* Problem path (Step 1): *"I dread tax season because my books are a mess."*
- Idea-only post: "Good bookkeeping reduces stress." (Nothing to do.)
- Usable post: **"Do this:** set up three folders today — *Income, Expenses, Set-Aside-for-Tax* — and forward every receipt to one email. Here's the 2-minute setup." Saveable (they'll redo it at tax time), shareable (every freelancer friend), beginner-simple.
- Loop: the version that opened with *"Why freelancers panic in April"* (a hook on the fear) beat the version that opened with *"Bookkeeping tips"* — same content, different first line.

## BUILD mode
1. Pull the problem + avatar. List 5–8 problem-path topics the buyer actually feels.
2. For each, write the promised result first, then a "do this / I did this" outline; add the save + share reason; simplify.
3. Write **3 hook variants** per topic (hook is the cheapest big lever).
4. Pick **one** format to start; set the output metric and the test cadence; set the batch gate ("stay at N until average ≥ X").
5. **Output:** a topic slate (topic → promised result → 3 hooks → format) + the loop rules. Point each piece's call-to-action at the lead magnet/funnel from **Step 5**. Save via `save_record("content_plan", …)`.

### Copy-paste AI prompt
```
You are an organic-content strategist. Business + locked problem statement: <paste from business-profile.yaml + Step 1>.
1) List 8 content topics that sit on the customer's problem path (problems the offer solves).
2) For the best 5, write "After watching they'll do ___ and get ___", then a short "do this" or "I did this" script.
3) For each, give a save-reason and a share-reason, and a beginner-simple rewrite.
4) Write 3 hook variants (first line / first 3 seconds) per topic.
5) Recommend ONE starting format and a test plan: which single variable to test first and how to read the result.
```

## AUDIT mode — rubric (used by /marketing-360)
Score the current content engine 0–10:
- **On the problem path + a human on screen** (not off-topic-viral, not faceless, not insider-only) — 3
- **Usable, not idea-only** (viewer knows what to do; saveable + shareable; simple) — 3
- **A real loop** (judged on one attention metric, one-variable tests, old-best → new-average trend) — 2
- **Points at the funnel** (a clear next step into the offer, not a dead end) — 2

🔴 0–4 (post-and-pray; views don't convert or don't come) · 🟡 5–7 (real content, no system) · 🟢 8–10 (a compounding engine feeding the funnel).
Red flags: faceless b-roll, abstract "tips" with no action, off-path viral chasing, batching before any signal, no CTA into the offer.

## Handoff
- **Feeds:** `5-build-the-funnel` (every post's action points into the funnel) and `7-launch-the-campaign` (the engine fills the room).
- **Then:** `9-close-with-emotion` converts the attention this engine earns.

---
*Credit: distills widely-taught organic-content and direct-response principles. Original wording and examples; no third-party material reproduced.*

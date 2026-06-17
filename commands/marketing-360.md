---
description: Run a Marketing 360 audit across all 7 Offer OS stations; find the weakest link and the top fixes.
argument-hint: "[offer, business, or 'profile' to read business-profile.yaml]"
---

# Marketing 360

Run a full-funnel audit of the target across the **7 Offer OS stations**. Because the stations are a chain, your job is to find **where it breaks** — the lowest-scoring link is the real bottleneck, and fixing it unlocks everything downstream.

## Target
`$ARGUMENTS`
If empty or "profile", read `business-profile.yaml` from the current directory (or nearest parent). If neither exists, ask the user for: the offer, the avatar, and the result they promise — nothing else.

## How to run
- For each station, score **0–10** and a **🔴/🟡/🟢** light against its test below.
- If the matching `offer-os:<n>-…` skill is installed, invoke it in **AUDIT mode**; otherwise apply the lens inline using its test.
- For a thorough audit, fan out one subagent per station in parallel, then synthesize.
- Be specific and honest — cite the exact words from the target that earn each score.

## The 7 lenses (test for each)

1. **Define the Problem** — Is the core problem a **short feeling in the customer's own words** that recurs both upstream and downstream? Red flag: a feature/benefit, or "-er" words. → `offer-os:1-define-the-problem`
2. **Position the Opportunity** — Is it a **new category (desire)** or just an **improvement (obligation)**? Run the 5 checks: different-not-better, wrong-shelf, removes-blame, carries-the-load, status-on-day-one. → `offer-os:2-position-the-opportunity`
3. **Build Your Frameworks** — Is there a **named, simple framework**, and does it cascade into a product ladder (flagship → paid offers → lead magnets → content)? Red flag: tactics with no named method. → `offer-os:3-build-your-frameworks`
4. **Build the Offer** — Is the offer a **problem-path stack** (one solution per real obstacle), sequenced to relieve objections, with a value-stacked price? Red flag: off-path bloat. → `offer-os:4-build-the-offer`
5. **Build the Funnel** — Is the **funnel type** right for the goal, and does the math work (average order value beats acquisition cost; break even up front)? → `offer-os:5-build-the-funnel`
6. **Add the Software Layer** — Is there a **single-purpose tool / software-as-bonus** (or at least a plan), or is it pure info buyers can now get from an AI for free? → `offer-os:6-add-the-software-layer`
7. **Launch the Campaign** — Is there a **one-to-many mechanism** (webinar/challenge) with **post-pitch follow-on bonuses** and an actual promo calendar — not just "post and pray"? → `offer-os:7-launch-the-campaign`

## Output — a one-page scorecard
1. A table: Station | Score /10 | 🔴/🟡/🟢 | the one sentence that explains the score.
2. **The weakest link** named as the bottleneck, with *why fixing it first unblocks the rest.*
3. **Top 3 fixes**, each mapped to the exact `offer-os:<n>` skill that fixes it, with the first concrete action.
4. One line: the single highest-leverage move this week.

Keep it tight and decisive — a scorecard the owner can act on today, not an essay.

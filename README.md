# Offer OS

A **numbered family of marketing skills** covering the **complete funnel** — from making attention, through building the offer in the order a business is actually built, to closing the sale. Stations **1–7** build the offer; stations **8** and **9** are the **attract** and **convert** bookends that wrap it.

```
        ── ATTRACT (top of funnel) ──
8  Build the Content Engine  ← an organic engine that makes attention, not random posts

        ── THE OFFER (build sequence) ──
1  Define the Problem        ← become the only answer
2  Position the Opportunity  ← sell desire, not "improvement"
3  Build Your Frameworks     ← turn knowledge into named methods + a product ladder
4  Build the Offer           ← problem-path stack, sequenced, value-priced
5  Build the Funnel          ← pick the flavor + make the math work
6  Add the Software Layer    ← a single-feature tool / software-as-bonus
7  Launch the Campaign       ← one-to-many promo with post-pitch follow-on bonuses

        ── CONVERT (bottom of funnel) ──
9  Close with Emotion        ← move the buyer through the beliefs that precede a yes
```

Plus **`/marketing-360`** — a complete full-funnel audit that scores all 9 stations (in funnel order **8 → 1–7 → 9**) on your current business and tells you **where the chain breaks** (your real bottleneck).

## Why it's built this way (portable across businesses)

- **Config over hardcode.** Nothing about a specific company lives in the skills. Fill in `business-profile.yaml` and the same skills run for a coach, an agency, an ecom store, or an insurance book.
- **Pluggable data.** Skills read/write through a `DataAdapter` (`_shared/profile.py`). The default `local` adapter needs zero infrastructure; swap in your own (CRM, a second brain) without touching a skill.
- **No secrets in skills.** Credentials live in your env/config, never in a `SKILL.md`.
- **Original & business-agnostic.** The skills distill widely-taught direct-response and offer-design principles into original wording with original illustrative examples — no third-party material is reproduced — so the family is yours to use, adapt, and share.

## Naming convention

`offer-os:<n>-<verb-noun>` — the namespace marks the family and the number marks the station. Stations **1–7** are the offer build sequence (each description says *"Step N of 7"*); stations **8** (attract) and **9** (convert) are the funnel bookends that wrap the build.

## Install & use

1. Copy `business-profile.example.yaml` → `business-profile.yaml` and fill it in.
2. (Optional, for the Python helpers) `pip install pyyaml`.
3. Install the plugin in Claude Code (it exposes the `offer-os:` skills and the `/marketing-360` command). The skills also work standalone — open any `skills/<step>/SKILL.md`.
4. Run the sequence in order, or run `/marketing-360` to audit first and fix the weakest link.

## Status

All 9 stations built, each with **build + audit modes** and a copy-paste AI prompt:

- ✅ `8-build-the-content-engine` — **attract bookend**: problem-path topics → usable scripting → test-and-scale loop
- ✅ `1-define-the-problem` — Problem Articulation + 11 worked examples
- ✅ `2-position-the-opportunity` — the Opportunity Switch (parking lot → fatal flaw → 5 tests)
- ✅ `3-build-your-frameworks` — name your method → product cascade
- ✅ `4-build-the-offer` — problem-path stack, sequenced, value-priced
- ✅ `5-build-the-funnel` — the 5 flavors + the math + high-ticket doc
- ✅ `6-add-the-software-layer` — single-feature tool / software-as-bonus
- ✅ `7-launch-the-campaign` — one-to-many launch w/ follow-on bonuses (+ orchestrator)
- ✅ `9-close-with-emotion` — **convert bookend**: the two-phase emotional journey to a yes
- ✅ `/marketing-360` — complete full-funnel audit across all 9 stations

## License

© 2026 Phillip Ngo. All rights reserved (proprietary). Public for visibility; not open-source. Contact for licensing or reuse.

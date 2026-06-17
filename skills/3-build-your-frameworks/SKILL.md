---
name: 3-build-your-frameworks
description: >-
  Step 3 of 7 in the Offer OS build sequence. Turns the expertise you already have into named,
  teachable frameworks — the engine inside every offer — then expands one framework into a full
  product ladder. Mines your transcripts/notes (via the data adapter) for the step-by-step paths
  you teach by instinct, names them, structures each as story -> principle -> how-to -> proof, and
  cascades them into flagship / paid-offer / lead-magnet / content layers. Triggers on "extract my
  frameworks", "name my method", "turn my knowledge into products", "I have no signature method",
  "package what I know", "build my product ladder". BUILD or AUDIT mode (used by /marketing-360).
  Reads business-profile.yaml.
---

# Step 3 — Build Your Frameworks

> A framework is the map of a path you've already walked — the repeatable steps you can hand to someone else. It's the engine *inside* the offer, not the offer itself. Your instinct about "what works" is usually a framework that just hasn't been named yet.

## Principles
- **Simple beats clever.** Complex frameworks confuse buyers and drive refunds — aim for ≤7 named steps, teachable in one sitting.
- **You have many.** Most experts carry a dozen un-named frameworks; surface them all, then pick a flagship.
- **Packaging sets the price.** The same method can be a cheap ebook, a course, a membership, or a high-ticket engagement — what changes is the wrapper, not the content.
- **Capture as you go.** The rules you scribble on a whiteboard already *are* frameworks; name and keep them.
- Call them whatever fits your brand: methods, blueprints, playbooks, protocols, systems.

## Teach every framework in four beats
**Story** (how you learned it) → **Principle** (why it works) → **How-to** (the steps) → **Proof** (a result). This is the reusable unit for slides, modules, emails, and talks.

## The product cascade
```
Flagship promise   = the one big outcome (your business)
Paid offers        = 3-4 core outcomes (what you sell)
Lead magnets       = ~10 small outcomes pulled from the cores (what you give to attract)
Content            = many micro-wins (one per post)
```
One named framework legitimately becomes a flagship promise, several offers, ten lead magnets, and endless content.

## BUILD mode
1. Use the adapter `get_transcripts()` to pull recordings/notes (or work from pasted material).
2. Detect the repeated step-by-step sequences the expert uses; draft a name + ≤7 steps for each.
3. Write each as story → principle → how-to → proof.
4. Pick the flagship and run the cascade.
5. **Output:** a named framework library + product-ladder map. Save via `save_record("frameworks", …)`; feed the flagship into **Step 4 (build the offer)**.

### Copy-paste AI prompt
```
You are a framework architect. Source: <paste transcripts/notes, or describe what you teach>.
1) Surface every distinct step-by-step METHOD the expert uses (look for repeated sequences/rules).
2) Name each (brandable, simple, <=7 steps); show the steps.
3) For the flagship, write it as Story -> Principle -> How-to -> Proof.
4) Run the cascade: 1 flagship promise, 3-4 paid offers, ~10 lead magnets, 15 content hooks — all from it.
Flag any framework too complex to teach in one sitting.
```

## AUDIT mode — rubric (used by /marketing-360)
0–10: a **named** signature framework exists (3) · it's **simple** (≤7 steps) (2) · taught with story + proof, not bare tactics (2) · it **cascades** into a ladder (3).
🔴 0–4 (tactics with no named method — you sound like everyone) · 🟡 5–7 (a method, not yet productized) · 🟢 8–10 (a named engine feeding a full ladder).

## Handoff
- **Prev:** the mechanism from `2-position-the-opportunity`. **Next:** `4-build-the-offer`.

---
*Credit: distills common knowledge-productization and curriculum-design principles. Original wording and examples; no third-party material reproduced.*

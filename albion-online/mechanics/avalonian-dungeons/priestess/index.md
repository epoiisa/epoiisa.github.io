---
layout: default
title: Priestess
permalink: /albiononline/mechanics/avalonian-dungeons/priestess/
---

# Avalonian Priestess (free boss)

| Stage | Health | Mechanics |
| ----- | ------ | --------- |
| 1 | 100–95% | Divine Authority, Divine Entrance, Divine Offering, Exorcism and Purify |
| 2 | 95–66% | Pity is added; each mark applies a 17-second lockout on the next cast |
| 3 | 66–33% | Pity’s lockout falls to 10 seconds |
| 4 | 33–0% | Pity’s lockout is removed; its 3-second base cooldown remains |
{: .nowrap-1 .nowrap-2 }

The health changes above affect **Pity**. The main encounter follows a repeating summon-and-purification cycle: **Divine Offering → Exorcism → Tainted Shadows → Purify**. Divine Entrance becomes available after **1 second**, Divine Offering after **6 seconds**, and Exorcism after **10 seconds** of combat. These are earliest eligibility times; casts and other actions can delay them. Pity’s shorter lockouts apply **below** 66% and 33%, respectively.

## Priestess’s abilities

- Divine Authority
- Divine Entrance
- Divine Offering
- Exorcism
- Divine Righteousness
- Pity
- Purify
- Tainted Shadows
  - Inner Corruption
  - Position Swap
  - Seeking Corruption
  - Shadow Nova
  - Sundered Defenses
  - Corrupting Essence

### Divine Authority

![Divine Authority](divine-authority.png)

A persistent protective effect greatly reduces damage the Priestess takes from players. Its **45-metre aura** also reduces players’ received healing by **70%**.

Her normal attacks **purge** their targets, removing purgeable buffs and healing effects. Every **five normal attacks** prepare an additional area purge against a player other than her highest-threat target. This has a **1.5-second cast** and affects a **4-metre-radius circle** around the selected player.

### Divine Entrance

![Divine Entrance](divine-entrance.png)

An opening **3-second cast** stuns enemies within **30 metres** for a base **1.5 seconds**. This is an opening effect rather than a repeating health phase.

### Divine Offering

![Divine Offering](divine-offering.png)

The Priestess creates a **5-metre-radius circle** at one of six positions around her. The active area lasts **35 seconds** and counteracts Divine Authority’s healing reduction while a player is inside it. New offerings use a shared **30-second base cooldown**, allowing a short overlap between areas.

Being inside this area also determines what **Exorcism** does to each player.

### Exorcism

![Exorcism](exorcism.png)

After a **3-second cast**, Exorcism checks players within **45 metres**. Each player inside Divine Offering produces a **Tainted Shadow** at their position, subject to a limit of **10 summoned shadows**. Each player outside Divine Offering instead grants the Priestess a stack of **Divine Righteousness**.

Exorcism has a **23-second base cooldown**, but its next cast also requires the previous cycle to have reached Purify. It does not continually summon new waves while the previous Exorcism remains active.

### Divine Righteousness

![Divine Righteousness](divine-righteousness.png)

Each stack increases the Priestess’s magic normal-attack damage by **5%** for **120 seconds** and supplies a recurring self-heal every **3 seconds** over the same duration. Multiple affected players can grant multiple stacks from one Exorcism.

### Pity

![Pity](pity.png)

Available from **95% health**. The Priestess marks a player other than her highest-threat target with an energy effect. After about **4 seconds**, it explodes, damaging enemies within **2.5 metres** of that player. The marked effect is purgeable.

Each mark applies a **17-second lockout** to the Priestess at 66% health or higher, or a **10-second lockout** below 66% but at or above 33%. These lockouts run alongside the ability’s **3-second base cooldown**, rather than being added to it. Below 33%, the extra lockout is absent. A marked player is also excluded from selection again for **10 seconds**.

### Purify

![Purify](purify.png)

After Exorcism, Purify becomes eligible when **one or fewer summoned shadows remain**. Following a **1-second cast**, the Priestess channels **10 pulses**, one per second, over a **45-metre radius**.

Each pulse checks for **Inner Corruption**. An affected player loses one stack, receives a base **1.2-second stun**, and triggers a damaging burst with a **50-metre radius** around them. Players with several stacks can trigger this effect on successive pulses. Purify also releases the encounter’s lock on the next Exorcism and has a **60-second base cooldown**.

## Tainted Shadows’ abilities

### Inner Corruption

![Inner Corruption](inner-corruption.png)

A Tainted Shadow’s normal attacks apply **Inner Corruption**, stacking up to **10 times**. These stacks are the condition for Purify’s damaging pulses and stuns. They can last up to **6 minutes**, but are cleared when the player is no longer affected by the Priestess’s Divine Authority aura.

### Position Swap

![Position Swap](position-swap.png)

A shadow can exchange positions with a player within **15 metres**, pulling that player to its own position while dashing to theirs. This becomes available **5 seconds after the shadow enters combat** and has a **20-second base cooldown**.

### Seeking Corruption

![Seeking Corruption](seeking-corruption.png)

Shadows link to other shadows within **5 metres**. Every **1.5 seconds**, a shadow heals nearby linked shadows for a base **5% of their maximum health**. Each nearby shadow also increases the recipient’s healing received, strengthening these mutual heals.

Links enable additional abilities: **two nearby shadows** can prepare Shadow Nova, while **five nearby shadows** can prepare Sundered Defenses.

### Shadow Nova

![Shadow Nova](shadow-nova.png)

Once enabled by nearby shadows, this ability becomes available after the caster has spent **15 seconds in combat**. A **1-second cast** creates a **5-metre-radius area** lasting **5 seconds**. Affected players receive damage ticks every **0.5 seconds**. The ability has an **8-second base cooldown**.

### Sundered Defenses

![Sundered Defenses](sundered-defenses.png)

Once enabled by nearby shadows, this ability becomes available after the caster has spent **10 seconds in combat**. Following a **1-second cast**, it reduces the current target’s bonus defence against mobs by **10% per stack**, up to **four stacks**, for **20 seconds**. It has a **4-metre range** and a **15-second base cooldown**.

### Corrupting Essence

![Corrupting Essence](corrupting-essence.png)

A slain Tainted Shadow releases a projectile toward the Priestess. Shadows killed close enough to her damage her and drain energy; shadows killed too far away instead heal her. This is a distance-dependent death effect, separate from the shadows’ normal attacks and area abilities.

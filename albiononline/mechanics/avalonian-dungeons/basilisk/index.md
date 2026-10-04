---
layout: default
title: Avalonian Crystal Basilisk
permalink: /albiononline/mechanics/avalonian-dungeons/basilisk/
---

# Avalonian Crystal Basilisk

| Stage | Health | Mechanics |
| ----- | ------ | --------- |
| 1 | 100–60% | Bite Attack, Petrify, Tailsmash and Cleansing Fire; Windwall becomes available at 90% |
| 2 | 60–0% | Earlier attacks continue except Windwall; adds Divine Overcharge, Divine Pulse, Divine Crystal Resonance and purifying circles |
{: .nowrap-1 .nowrap-2 }

Petrify and rear-target checks for Tailsmash begin after **10 seconds**. Cleansing Fire becomes available after **30 seconds**. These timers are independent of the 60% stage transition. The Basilisk's passive health regeneration stops when stage 2 begins.

## Basilisk’s abilities

- Bite Attack
- Petrify
- Tailsmash
- Cleansing Fire → Holy Flames
- Windwall
- Divine Overcharge → Divine Pulse
- Divine Crystal Resonance
- Purifying circle

### Bite Attack

![Bite Attack](assets/bite-attack.png)

A physical bite against the current target, with roughly **1 second before impact**. Successful hits apply a stacking **Dissolving Saliva** effect: each stack reduces the player's defence against mobs by **3%**, up to **50 stacks**.

The effect has a long duration and accumulates during the fight. It is explicitly removed by the purifying circle. Leaving the Basilisk’s **30-metre engagement aura** also allows the periodic cleanup to remove it.

### Petrify

![Petrify](assets/petrify.png)

After a **2-second cast**, the Basilisk petrifies players in a **60-degree cone** extending roughly **30 metres** in front of it. Petrification is a cleansable stun with a **10-second base duration**. The attack is an area effect, not a check of which direction a player is facing.

### Tailsmash

![Tailsmash](assets/tailsmash.png)

A player detected behind the Basilisk can trigger a tail attack. After approximately **0.6 seconds**, it hits a **45-degree rear cone** extending from roughly **4 to 30 metres**, dealing physical damage and knocking victims back about **10 metres**.

The rear detection area is smaller than the attack itself: the trigger checks roughly **4–15 metres** behind the boss.

### Cleansing Fire

![Cleansing Fire](assets/cleansing-fire.png)

The Basilisk casts for **1.7 seconds**, then sweeps a narrow cone of fire from side to side for **3.5 seconds**. The breath reaches roughly **26 metres** and deals repeated magic damage; a player can be hit again after **0.5 seconds**.

Damaging hits apply **Holy Flames**, which ticks every **3 seconds** for about **45 seconds**. It stacks twice. One stack causes a small lingering burn; **two stacks change the burn to a much larger magic-damage tick**.

### Windwall

![Windwall](assets/windwall.png)

Available between **90% and 60% health**. After a **2-second cast**, two curved walls expand outward from opposite sides of the Basilisk for **5 seconds**, reaching approximately **25 metres**.

Contact knocks players outward about **15 metres** and deals magic damage. This ability stops being selected once stage 2 begins.

### Divine Overcharge

![Divine Overcharge](assets/divine-overcharge.png)

In stage 2, the Basilisk charges up and sends lightning through up to **seven distinct players**. The sequence has a **2.7-second cast** followed by a **3-second impact delay**. Each affected player takes an initial hit and gains **Divine Overcharge**.

Each stack increases the player's damage against mobs by **20%** and reduces their defence against mobs by **20%**. The effect also produces Divine Pulse. Repeated applications stack, and the purifying circle removes the effect.

Each charge-up separately gives the Basilisk a permanent, stacking **5% bonus defence against players** for the remainder of the encounter.

### Divine Pulse

![Divine Pulse](assets/divine-pulse.png)

An overcharged player releases the first pulse after **1.5 seconds**, then another every **5 seconds**. Each pulse affects a **5-metre radius** around that player.

The pulse's damage checks require its victim to have Divine Overcharge. Other overcharged players within range can therefore be hit by the same pulse. Damage increases with the victim's Overcharge stacks, with the highest listed damage bracket beginning at **five stacks**.

### Divine Crystal Resonance

![Divine Crystal Resonance](assets/divine-crystal-resonance.png)

After a **0.6-second cast**, the Basilisk strikes players within roughly **30 metres**. Each struck player is the centre of a further **3-metre-radius damage effect**, so overlapping impacts can hit nearby players more than once. The damage interrupts casting.

### Purifying circle

![Purifying circle](assets/purifying-circle.png)

Stage 2 marks a player with a **4-metre-radius circle**. After **5 seconds**, the circle activates for about **1.2 seconds**.

Players inside lose **Divine Overcharge** and **Dissolving Saliva**. The effect also purges removable beneficial effects, including applicable buffs, healing-over-time effects, movement buffs and shields. It does **not** remove or apply Holy Flames. Friendly creatures of the boss instead receive a cleanse.

*Purifying circle is a descriptive label for this mechanic; the installed client does not supply an English ability name for its cast.*

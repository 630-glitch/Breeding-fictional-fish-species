# 🐟 Breeding Fictional Fish Species

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=python)](https://pygame.org)
[![License](https://img.shields.io/github/license/630-glitch/Breeding-fictional-fish-species)](LICENSE)
[![Help Wanted](https://img.shields.io/badge/help--wanted-orange)](https://github.com/630-glitch/Breeding-fictional-fish-species/issues)

**Breed, evolve and experiment with fictional fish species in a living ecosystem.**

This is a genetic simulation in Pygame where each fish has its own DNA — passed down, mutated, and shaped by its environment. Fish have immune systems, personalities, social behaviors, and can learn from interactions. The water itself affects their health.

> **Status**: Prototype / Work in Progress. Core systems work but need polishing, fixing and finishing. Contributions welcome!

---

## 🧬 Features

### Genetics & Breeding
- **4 chromosome pairs** (ch1–ch4) controlling appearance, behavior and metabolism
- **Multi-generation breeding** with genetic crossover during reproduction
- **Heritable traits**: body color, fin shape (circular/triangular), tail type, eye size, pupil color, mouth size, and more
- **Sexual reproduction** with two parent gene mixing

### Immune System
- **Bacteria ecosystem** (`dr`, `in`, `frin`, `dir` types) that infect fish
- Fish with strong immune genes fight off infections
- Bacteria evolve and spread through the tank

### Ecosystem
- **3 food types**: yellow (basic), white (hardness), orange (nutritious)
- **Oxygen levels** — fish suffer if oxygen drops too low
- **Water hardness** — each fish has a preferred range; outside it, health degrades
- Fish can starve, get injured, or die from poor conditions

### Behavior & Learning
- Fish **learn from clicks** (tap = positive, near = avoid)
- **Social behavior** — fish see each other, school together, or fight
- **Memory system** — fish remember recent events (being bitten, finding food)
- **Personality traits** that change movement patterns

### Visual
- Real-time Pygame rendering with colored fish sprites
- Visual indicators for health, injury, and status
- Egg incubation with color-coded health
- Multiple tank support

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame

```bash
pip install pygame
```

### Run

```bash
git clone https://github.com/630-glitch/Breeding-fictional-fish-species.git
cd Breeding-fictional-fish-species
python j_add.py
```

### Controls

| Action | Description |
|---|---|
| **Click a fish** | Open fish info panel |
| **Click a colored square** | Spawn food (red = yellow food, orange = white food) |
| **Click menu button** | Open game menu |
| **Drag a fish** | Move it around the tank |

---

## 📁 Project Structure

```
Breeding-fictional-fish-species/
├── j_add.py       # Main game loop, event handling, world update
├── fch_draw.py    # Fish and egg rendering (Pygame drawing)
├── f_int.py       # Genetics logic (egg creation, crossover, trait checks)
├── popups.py      # UI popup menus and dialogs
├── my_mod.py      # Math helpers (middle point calculation)
├── f_draw.py      # Dead fish rendering (not currently used)
├── README.md
└── LICENSE
```

---

## 🧪 Current State

The prototype works but has known issues:

- Some functions reference undeclared variables (e.g. `isfin()` in `f_int.py`)
- Genetics use raw lists with magic indexes — hard to read and maintain
- Code duplication between files (e.g. `f_int.py` and `j_add.py` both define `egg`, `fry`, `isfin`)
- JSON trait persistence (`traits5.json`) is reset on every launch
- UI popups show placeholder text ("mesage3", "message1") instead of real labels
- No error handling for missing attributes or invalid states

### What's needed most

| Priority | Task |
|---|---|
| 🥇 | Fix critical bugs (variable scope in `f_int.py`, `fry.move()` in `j_add.py`) |
| 🥇 | Replace magic-index lists with named attributes/classes |
| 🥈 | Clean up global state and file organization |
| 🥈 | Add proper UI text and labels |
| 🥉 | Implement real-time genetics display |
| 🥉 | Add save/load functionality that actually persists |

---

## 🤝 Contributing

The original author says:
> *"Needs finishing, improvement and fixing. This is a prototype and working alone became a problem. I'd love to see what can be done with this project."*

All contributions are welcome! Feel free to:
- Open an issue for bugs or ideas
- Fork and submit a PR
- Refactor the genetics system into something cleaner

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

*Built with ❤️ by [630-glitch](https://github.com/630-glitch)*

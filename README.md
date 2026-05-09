# Kingdom's Last Stand

<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.13-4B8BBE?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.13" />
  <img src="https://img.shields.io/badge/PYGAME-2.6+-2E8B57?style=for-the-badge&logo=pygame&logoColor=white" alt="Pygame" />
</p>

<p align="center">
  <b>A fantasy tower defense game built with Python and Pygame.</b><br/>
  Defend the castle, place towers with limited gold, survive escalating waves, and review polished end-of-session battle stats.
</p>

---

## Project Description

- **Project by:** Thanutdit Jiravichalert
- **Game Genre:** Strategy, Tower Defense

Kingdom's Last Stand is a single-player wave-based tower defense game. The player defends a castle by placing Archer, Mage, and Cannon towers on a map to stop 10 escalating waves of enemies. Each wave enemies grow stronger and faster, and every gold coin spent matters. After each session, all gameplay data is saved to a CSV file and can be reviewed in an interactive Statistics screen with 6 data visualizations.

---

## Installation

Clone this project:

```sh
git clone https://github.com/thanutdit-ku/GameYear1Project.git
cd GameYear1Project
```

Create and activate a Python virtual environment, then install dependencies:

**Mac:**
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running Guide

After activating the virtual environment, run the game:

**Mac:**
```sh
python3 main.py
```

**Windows:**
```bat
python main.py
```

### Running Tests

The test suite covers `StatsTracker` and the game's statistics logic. No display or Pygame window is required to run tests.

**Mac:**
```sh
python3 -m pytest tests/ -v
```

**Windows:**
```bat
python -m pytest tests/ -v
```

To run a specific test file:

**Mac:**
```sh
python3 -m pytest tests/test_stats_tracker.py -v
python3 -m pytest tests/test_game_stats.py -v
```

**Windows:**
```bat
python -m pytest tests/test_stats_tracker.py -v
python -m pytest tests/test_game_stats.py -v
```

Expected output:
```
101 passed in 0.47s
```

| Test File | What It Covers |
|---|---|
| `tests/test_stats_tracker.py` | Recording kills/damage/gold, CSV writes, history, `generate_report` |
| `tests/test_game_stats.py` | Player stat aggregation, efficiency calculation, edge cases |

Tests also run automatically on every push via GitHub Actions.

---

## Tutorial / Usage

1. **Launch the game** — run `main.py`
2. **Enter your Commander name** in the text box on the Home screen
3. **Select a map** — choose from 6 maps, each with a unique enemy path
4. **Click Start Campaign** to begin
5. **Place towers** — click a tower in the Armory panel (or press `1` / `2` / `3`), then click a green tile on the map
6. **Click Start Wave** to release enemies
7. **Earn gold** by defeating enemies, then spend it on new towers or upgrades
8. **Right-click** a placed tower to cycle its targeting mode (First / Last / Strongest / Closest)
9. **Press `F`** and click a tower to sell it
10. **Press `P`** to pause, **`ESC`** to clear selection
11. **Survive all 10 waves** to achieve Victory
12. From the Home screen, click **Statistics** to review all session data across 6 graphs

---

## Game Features

- **3 tower types** with distinct roles:
  - `Archer` — fast attacks with 20% critical hit chance
  - `Mage` — slows enemies by 50% for 2 seconds on hit
  - `Cannon` — area splash damage in a 50px radius
- **4 targeting modes** per tower — First, Last, Strongest, Closest (right-click to cycle)
- **9 enemy types** — Slime (splits on death), Goblin, Bat, SwordShield, Orc, Spider, DarkKnight, Boss Dragon
- **10 waves** with HP scaling (×1.20 per wave) and speed scaling (×1.10 per wave)
- **Boss waves** — Dragon with 750 HP appears on Wave 5 and Wave 10
- **6 playable maps** — Royal Road, Twin Bend, Southern Pass, Stone Spiral, Ember Valley, Frost Crossing
- **Automatic CSV data recording** — every wave saved to `data/game_stats.csv`
- **Interactive Statistics screen** with 6 visualizations:
  - Summary Table (Mean, Median, Std Dev, Min, Max)
  - Leaderboard
  - Gold vs Wave scatter plot
  - Damage Efficiency bar chart
  - Survival Curve line chart
  - Wave Survival Heatmap

---

## Known Bugs

- No have

---

## Unfinished Works

- Tower sell refund is a flat rate; a percentage-based refund was planned but not implemented
- The Statistics screen has no filter by map or player — all sessions are always aggregated together

---

## External Sources

### Libraries and Frameworks

| Library | Version | Purpose | License |
|---|---|---|---|
| [Pygame](https://www.pygame.org/) | 2.6+ | Game engine, rendering, input | LGPL |
| [matplotlib](https://matplotlib.org/) | 3.7+ | In-game statistical charts | PSF/BSD |
| [pandas](https://pandas.pydata.org/) | 2.0+ | CSV loading and summary statistics | BSD |
| [Python](https://www.python.org/) | 3.10+ | Language | PSF |

### Art and Sprites

All sprites are used under their respective free/open licenses. Frame counts and sheet dimensions are as loaded in-game.

#### Tower Sprites

| Tower | File(s) | Format | Details | Source |
|---|---|---|---|---|
| **Archer Tower** | `assets/images/towers/archer/Idle/` | 10 individual PNGs (1024×1024) | Idle animation — 10 frames | [2D Animated Archer Spritesheet — OpenGameArt](https://opengameart.org/content/2d-animated-archer-spritesheet) |
| **Archer Tower** | `assets/images/towers/archer/Shoot_Stand/` | 22 individual PNGs (1024×1024) | Shoot animation — 22 frames | [2D Animated Archer Spritesheet — OpenGameArt](https://opengameart.org/content/2d-animated-archer-spritesheet) |
| **Archer Tower** | `assets/images/towers/archer/Jump/` | 22 individual PNGs (1024×1024) | Jump animation — 22 frames | [2D Animated Archer Spritesheet — OpenGameArt](https://opengameart.org/content/2d-animated-archer-spritesheet) |
| **Archer Tower** | `assets/images/towers/archer/Run_Idle/` | 22 individual PNGs (1024×1024) | Run-idle animation — 22 frames | [2D Animated Archer Spritesheet — OpenGameArt](https://opengameart.org/content/2d-animated-archer-spritesheet) |
| **Mage Tower** | `assets/images/enemies/dark_knight/mage/AttackMighty1–6.png` | 6 individual PNGs (32×32, scaled 2×) | Cast animation — 6 frames | [Pixel Art Assets 5 — greenpixels (itch.io)](https://greenpixels.itch.io/pixel-art-assets-5) |
| **Cannon Tower** | `assets/images/enemies/dark_knight/Cannon/cannon-sheet.png` | Sprite sheet 512×64 | 8 frames × 64×64 px in a single row | [Cannon Gun Sprite Animated — OpenGameArt](https://opengameart.org/content/cannon-gun-sprite-animated) |

#### Enemy Sprites

| Enemy | File(s) | Format | Details | Source |
|---|---|---|---|---|
| **Slime / MiniSlime** | `assets/images/enemies/slime/slime-move-0–3.png` | 4 individual PNGs (32×25) | Walk animation — 4 frames, MiniSlime uses same frames scaled down | [Pixel Art Animated Slime — rvros (itch.io)](https://rvros.itch.io/pixel-art-animated-slime) |
| **Wolf** | `assets/images/enemies/goblin/howl.png` | Single PNG (64×64) | Static sprite, no animation | [LPC Wolf Animation — OpenGameArt](https://opengameart.org/content/lpc-wolf-animation) |
| **Bat** | `assets/images/enemies/goblin/bat.png` | Sprite sheet (128×128) | Directional fly animation | [Bat Sprite — OpenGameArt](https://opengameart.org/content/bat-sprite) |
| **SwordShield** | `assets/images/enemies/swordshield/walk.png` | Sprite sheet 336×42 | 8 frames × 42×42 px — walk cycle | [Knight Sprite — lionheart963 (itch.io)](https://lionheart963.itch.io/knight-sprite) |
| **SwordShield** | `assets/images/enemies/swordshield/idle.png` | Sprite sheet 168×42 | 4 frames × 42×42 px — idle cycle | [Knight Sprite — lionheart963 (itch.io)](https://lionheart963.itch.io/knight-sprite) |
| **Orc** | `assets/images/enemies/orc/orc_walk.png` | Sprite sheet 320×320 | 10 columns × 32×32 px per frame — walk cycle, displayed at 48×48 | [Animated Orcs — OpenGameArt](https://opengameart.org/content/animated-orcs) |
| **Spider** | `assets/images/enemies/spider/walk.png` | Sprite sheet 640×320 | 4 rows (up/left/down/right) × 10 cols × 64×64 px — directional walk | [LPC Spider — OpenGameArt](https://opengameart.org/content/lpc-spider) |
| **DarkKnight** | `assets/images/enemies/dark_knight/FreeKnight/_Idle.png` | Sprite sheet 1200×80 | 10 frames × 120×80 px — idle animation | [Fantasy Knight — aamatniekss (itch.io)](https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character) |
| **DarkKnight** | `assets/images/enemies/dark_knight/FreeKnight/_Run.png` | Sprite sheet 1200×80 | 10 frames × 120×80 px — run animation | [Fantasy Knight — aamatniekss (itch.io)](https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character) |
| **DarkKnight** | `assets/images/enemies/dark_knight/FreeKnight/_Death.png` | Sprite sheet 1200×80 | 10 frames × 120×80 px — death animation | [Fantasy Knight — aamatniekss (itch.io)](https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character) |
| **Dragon Boss** | `assets/images/enemies/boss/dragon.png` | Sprite sheet 432×512 | 3 cols × 4 rows × 144×128 px — directional walk (N/E/S/W) | [Flying Dragon Rework — OpenGameArt](https://opengameart.org/content/flying-dragon-rework) |



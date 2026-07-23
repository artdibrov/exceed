# ASCII Map Builder

ASCII Map Builder is a lightweight Python application for creating procedural maps suitable for roguelike games.

The application generates dungeon-like layouts using simple algorithms, validates connectivity and exports maps as plain text.

## Features

- Procedural map generation
- Random room placement
- Corridor creation
- ASCII rendering
- Connectivity validation
- Map statistics

## Symbols

| Symbol | Meaning |
|--------|---------|
| # | Wall |
| . | Floor |
| + | Door |
| ~ | Water |
| ^ | Trap |
| @ | Player |

## Example

###########
#.........#
#..###....#
#..#@#....#
#..###..^.#
#.....+...#
###########

Run

```bash
python main.py
```

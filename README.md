# Gomoku Game

A modern, feature-rich implementation of the classic Gomoku game using Python and Pygame.

## Features
- Modular codebase: separate files for game logic, AI, and GUI
- Human vs AI and Human vs Human modes
- Start menu with player color and AI difficulty selection
- Restart option after each game
- Highlights last move and shows winning line
- Sound effects for moves and win/loss
- AI with three difficulty levels (Easy, Medium, Hard)
- Well-documented code with descriptive variable names

## Installation
1. Make sure you have Python 3.x installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository.

## Usage
Run the game from the project folder:
```bash
python gomoku.py
```

## How to Play
- Select game mode, player color, and AI difficulty from the start menu.
- Click on the board to place your piece.
- The game will highlight the last move and show a green line when someone wins.
- Press 'R' to restart or 'Q' to quit after a game ends.

## File Structure
- `gomoku.py` - Main entry point
- `game_logic.py` - Board management and win detection
- `ai_logic.py` - AI move selection and evaluation
- `gui.py` - Pygame graphical interface
- `GUI_Pic/` - Images for board and pieces

## Screenshots
_Add your screenshots here_

## Credits
- Original project by RaTuL
- Improvements and refactoring by GitHub Copilot

## License
MIT

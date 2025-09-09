# Gomoku Game

A modern, feature-rich implementation of the classic Gomoku game using Python and Pygame.

## GitHub Repository
[TM-Mehrab-Hasan/Gomoku-Game-Using-Python](https://github.com/TM-Mehrab-Hasan/Gomoku-Game-Using-Python.git)

## Features
- **Standalone Executable**: Ready-to-run .exe file with no installation required
- **Modular codebase**: Separate files for game logic, AI, and GUI
- **Dual game modes**: Human vs AI and Human vs Human
- **Interactive menus**: Mouse and keyboard support for all selections
- **Step-by-step setup**: Game mode → Color → AI difficulty selection
- **Player customization**: Choose to play as Black or White pieces
- **AI difficulty levels**: Easy (random), Medium (strategic), Hard (advanced)
- **Visual enhancements**: 
  - Highlights last move with red circle
  - Shows winning line in green
  - Clean, wood-themed interface design
- **Sound effects**: Audio feedback for moves and wins
- **Restart functionality**: Quick restart option after each game
- **Well-documented code**: Clear comments and modular structure

## Installation

### Option 1: Run the Standalone Executable (Recommended)
1. Download the `GomokuGame.exe` from the `dist` folder
2. Double-click to run - no installation required!
3. The executable includes all dependencies and works on any Windows computer

### Option 2: Run from Source Code
1. Make sure you have Python 3.x installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository

## Usage

### Using the Standalone Executable:
- Simply double-click `GomokuGame.exe` in the `dist` folder
- No Python installation required

### Running from Source:
```bash
python gomoku.py
```

### Building Your Own Executable:
If you want to create your own executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name=GomokuGame --add-data="GUI_Pic;GUI_Pic" gomoku.py
```
Or simply run the provided `build.bat` file

## How to Play
- **Menu Navigation**: Use mouse clicks or keyboard keys to navigate menus
- **Game Mode**: Choose between Human vs AI or Human vs Human
- **Color Selection**: Pick Black or White pieces (visual selection with sample stones)
- **AI Difficulty**: Select Easy (random), Medium (basic strategy), or Hard (advanced tactics)
- **Gameplay**: Click on the board to place your piece
- **Visual Feedback**: Last move is highlighted with a red circle
- **Win Detection**: Winning line is shown in green when game ends
- **Restart**: Press 'R' to restart or 'Q' to quit after a game ends

## File Structure
- `gomoku.py` - Main entry point
- `game_logic.py` - Board management and win detection
- `ai_logic.py` - AI move selection and evaluation
- `gui.py` - Pygame graphical interface with step-by-step menus
- `GUI_Pic/` - Images for board and pieces
- `dist/GomokuGame.exe` - Standalone executable (ready to run)
- `build.bat` - Quick build script for creating new executables
- `build_exe.py` - Python build script
- `GomokuGame.spec` - PyInstaller configuration

## Distribution
The game comes with a pre-built standalone executable:
- **Location**: `dist/GomokuGame.exe`
- **Size**: ~30MB (includes all dependencies)
- **Requirements**: Windows (no Python installation needed)
- **Portable**: Can be copied to any Windows computer and run immediately

## Screenshots
_Add your screenshots here_

## Development Notes
- Built with Python 3.13.5 and Pygame 2.6.1
- Uses PyInstaller for executable creation
- Modular architecture for easy maintenance and feature additions
- Step-by-step menu system for better user experience
- Error handling for sound effects to prevent crashes

## Credits
- Original project by RaTuL (2021 - 3rd semester university project)
- Improvements and refactoring by GitHub Copilot (2025)
- Enhanced with modern UI, mouse support, and standalone distribution

## License
MIT

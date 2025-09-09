# 🎯 Gomoku Game - Five in a Row Strategy Game

A sophisticated, modern implementation of the classic Gomoku (Five in a Row) strategy game built with Python and Pygame. Features intelligent AI opponents, beautiful graphics, and a polished user experience.

![Python](https://img.shields.io/badge/python-v3.13.5-blue)
![Pygame](https://img.shields.io/badge/pygame-v2.6.1-green)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🎮 Game Overview

Gomoku, also known as Five in a Row, is an abstract strategy board game played on a 15×15 grid. The objective is to be the first player to form an unbroken chain of five stones horizontally, vertically, or diagonally. This implementation combines traditional gameplay with modern features and AI opponents.

## ✨ Key Features

### 🎯 Core Gameplay
- **Classic Gomoku Rules**: Traditional 15×15 board with win condition of 5 stones in a row
- **Dual Game Modes**: Challenge AI opponents or play local multiplayer
- **Strategic AI**: Three difficulty levels with varying intelligence and tactics
- **Visual Win Detection**: Automatic highlighting of winning combinations

### 🖱️ User Interface & Experience
- **Intuitive Step-by-Step Setup**: Guided menu system for game configuration
- **Dual Input Support**: Both mouse clicks and keyboard shortcuts
- **Visual Stone Selection**: Preview black/white pieces before selection
- **Move Highlighting**: Red circle indicates the last move played
- **Win Line Display**: Green line shows the winning five-stone sequence
- **Wood-Themed Aesthetics**: Professional board design with realistic textures

### 🤖 Artificial Intelligence
- **Easy Mode**: Random placement with basic validity checking
- **Medium Mode**: Strategic evaluation with pattern recognition
- **Hard Mode**: Advanced tactics with threat analysis and blocking

### 🔧 Technical Excellence
- **Modular Architecture**: Clean separation of game logic, AI, and presentation
- **Standalone Distribution**: Self-contained executable requiring no installation
- **Cross-Platform Codebase**: Python source runs on Windows, macOS, and Linux
- **Sound Integration**: Audio feedback for moves and game events
- **Error Resilience**: Robust handling of edge cases and user input

## 🚀 Quick Start

### Option 1: Instant Play (Recommended)
1. Download `GomokuGame.exe` from the [`dist`](./dist) folder
2. Double-click to launch - no installation required!
3. Enjoy the game on any Windows computer

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/your-username/gomoku-game.git
cd gomoku-game

# Install dependencies
pip install pygame

# Launch the game
python gomoku.py
```

### Option 3: Build Your Own Executable
```bash
# Install build tools
pip install pyinstaller

# Create standalone executable
pyinstaller --onefile --windowed --name=GomokuGame --add-data="GUI_Pic;GUI_Pic" gomoku_standalone.py
```

## 🎯 How to Play

### Game Setup
1. **Mode Selection**: Choose Human vs AI or Human vs Human
2. **Color Choice**: Select Black (first player) or White (second player)  
3. **AI Difficulty**: Pick Easy, Medium, or Hard (if playing vs AI)

### Gameplay Mechanics
- **Placing Stones**: Click any empty intersection on the board
- **Turn System**: Players alternate placing stones
- **Victory Condition**: First to achieve 5 stones in a row wins
- **Visual Feedback**: Last move highlighted, winning line displayed

### Controls
- **Mouse**: Click to place stones and navigate menus
- **Keyboard Shortcuts**: 
  - `1`/`2` for game mode selection
  - `B`/`W` for color selection  
  - `E`/`M`/`H` for difficulty selection
  - `R` to restart, `Q` to quit

## 📁 Project Structure

```
gomoku-game/
├── 📁 GUI_Pic/           # Game assets (board, stones)
│   ├── bg.png           # Board background texture
│   ├── black.png        # Black stone sprite
│   └── white.png        # White stone sprite
├── 📁 dist/             # Compiled executables
│   └── GomokuGame.exe   # Standalone Windows executable
├── 📄 gomoku.py         # Main application entry point
├── 📄 game_logic.py     # Board state and win detection
├── 📄 ai_logic.py       # AI algorithms and difficulty levels
├── 📄 gui.py            # Pygame interface and menu system
├── 📄 gomoku_standalone.py # All-in-one file for building
└── 📄 README.md         # Project documentation
```

## 🎨 Architecture Design

### Modular Components
- **`game_logic.py`**: Pure game state management, win detection algorithms
- **`ai_logic.py`**: AI decision-making engine with configurable difficulty
- **`gui.py`**: Pygame-based rendering, input handling, and menu systems
- **`gomoku.py`**: Application orchestration and module integration

### Design Patterns
- **Model-View Architecture**: Clear separation between game logic and presentation
- **Strategy Pattern**: Pluggable AI difficulty implementations
- **Observer Pattern**: Event-driven updates for move validation and win detection

## 🤖 AI Implementation Details

### Easy Mode (Beginner-Friendly)
- Random move selection with validity checking
- No strategic evaluation or pattern recognition
- Ideal for new players learning the game

### Medium Mode (Balanced Challenge)
- Basic positional evaluation
- Simple pattern recognition for common formations
- Reactive play with some forward planning

### Hard Mode (Advanced Strategy)
- Sophisticated threat analysis and response
- Multi-move lookahead capabilities
- Proactive formation building and opponent blocking

## 🔧 Development & Deployment

### Local Development
```bash
# Set up virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install pygame pyinstaller

# Run in development mode
python gomoku.py
```

### Building for Distribution
```bash
# Create optimized executable
pyinstaller --onefile --windowed --name=GomokuGame --add-data="GUI_Pic;GUI_Pic" gomoku_standalone.py

# Executable will be created in dist/GomokuGame.exe
```

## 📊 Technical Specifications

- **Language**: Python 3.13.5
- **Graphics Library**: Pygame 2.6.1
- **Build Tool**: PyInstaller 6.15.0
- **Target Platform**: Windows 10/11 (64-bit)
- **Executable Size**: ~30MB (self-contained)
- **Memory Usage**: ~50MB runtime
- **Dependencies**: None (standalone executable)

## 🏆 Credits & Acknowledgments

- **Original Concept**: Traditional Gomoku game rules and mechanics
- **Initial Implementation**: RaTuL (University project, 2021)
- **Modern Enhancement**: Comprehensive refactoring and feature expansion
- **AI Development**: Strategic algorithms and difficulty balancing
- **UI/UX Design**: Professional interface and user experience improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
and professional game mechanics. Built with Python & Pygame.

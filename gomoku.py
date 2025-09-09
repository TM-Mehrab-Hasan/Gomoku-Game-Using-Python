"""
Main entry point for Gomoku Game.
Imports game logic, AI, and GUI modules and starts the game.
"""

from game_logic import Board
from gui import GomokuGUI

def main():
    board = Board()
    gui = GomokuGUI(board)
    gui.run()

if __name__ == "__main__":
    main()
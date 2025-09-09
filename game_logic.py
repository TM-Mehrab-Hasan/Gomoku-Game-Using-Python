"""
Game logic for Gomoku: board management, win detection, move validation.
"""

BOARD_SIZE = 15

class Board:
    """
    Represents the Gomoku board and provides methods for placing pieces,
    checking for empty cells, and win detection.
    """
    def __init__(self):
        """Initialize an empty BOARD_SIZE x BOARD_SIZE grid."""
        self.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def place(self, x, y, color):
        """
        Place a piece of the given color at (x, y).
        Returns True if successful, False if invalid move.
        """
        if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
            return False
        if self.grid[x][y] != 0:
            return False
        self.grid[x][y] = color
        return True

    def is_empty(self, x, y):
        """Return True if cell (x, y) is empty."""
        return self.grid[x][y] == 0

    def check_win(self, x, y, color, length=5):
        """
        Check if placing at (x, y) wins the game for color.
        Returns True if there are 'length' consecutive pieces of the same color.
        """
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            count = 1
            # Check in the positive direction
            for step in range(1, length):
                nx, ny = x + dx*step, y + dy*step
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.grid[nx][ny] == color:
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, length):
                nx, ny = x - dx*step, y - dy*step
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.grid[nx][ny] == color:
                    count += 1
                else:
                    break
            if count >= length:
                return True
        return False

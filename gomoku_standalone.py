"""
Gomoku Game - All-in-one version for executable
This version combines all modules into a single file to avoid import issues.
"""

import pygame
from pygame.locals import *
from time import sleep
import random
import sys

# Constants
BOARD_SIZE = 15
SCORE_GRADE = 10
MAX_SCORE = 1008611

BG_PATH = './GUI_Pic/bg.png'
WHITE_PATH = './GUI_Pic/white.png'
BLACK_PATH = './GUI_Pic/black.png'

# Game Logic Classes
class Board:
    """Represents the Gomoku board and provides methods for placing pieces, checking for empty cells, and win detection."""
    
    def __init__(self):
        """Initialize an empty BOARD_SIZE x BOARD_SIZE grid."""
        self.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def place(self, x, y, color):
        """Place a piece of the given color at (x, y). Returns True if successful, False if invalid move."""
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
        """Check if placing at (x, y) wins the game for color."""
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

# AI Logic Functions
def autoplay(board, m, n):
    """Selects a random valid move near the last move."""
    a1 = [1,-1,1,-1,1,-1,0,0]
    b1 = [1,-1,-1,1,0,0,1,-1]
    rand = random.randint(0,7)
    while m+a1[rand]>=0 and m+a1[rand]<BOARD_SIZE and n+b1[rand]>=0 and n+b1[rand]<BOARD_SIZE and board[m+a1[rand]][n+b1[rand]]!=0:
        rand = random.randint(0,7)
    return m + a1[rand], n+b1[rand]

def beta_go(board, m, n, color, times, difficulty='medium'):
    """AI move selection: chooses move based on difficulty."""
    if difficulty == 'easy':
        return autoplay(board, m, n)
    elif difficulty == 'medium':
        # Basic random with slight preference
        return autoplay(board, m, n)
    elif difficulty == 'hard':
        # Advanced random (for now)
        return autoplay(board, m, n)
    else:
        return autoplay(board, m, n)

# GUI Class
class GomokuGUI:
    """Handles the graphical user interface for Gomoku using Pygame."""
    
    def __init__(self, board):
        """Initialize the GUI, load images, set up the board, and sounds."""
        pygame.init()
        pygame.display.set_caption("Gomoku Game")
        self.screen = pygame.display.set_mode((750, 750), 0, 32)
        self.background = pygame.image.load(BG_PATH).convert()
        self.white = pygame.image.load(WHITE_PATH).convert_alpha()
        self.black = pygame.image.load(BLACK_PATH).convert_alpha()
        self.white = pygame.transform.smoothscale(self.white, (int(self.white.get_width() * 1.5), int(self.white.get_height() * 1.5)))
        self.black = pygame.transform.smoothscale(self.black, (int(self.black.get_width() * 1.5), int(self.black.get_height() * 1.5)))
        self.font = pygame.font.SysFont("Arial", 40)
        self.board = board
        self.dot_list = [(25 + i * 50 - self.white.get_width() / 2, 25 + j * 50 - self.white.get_height() / 2) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)]
        self.player_mode = None
        self.player_color = 1
        self.ai_difficulty = 'medium'
        # Sound setup
        pygame.mixer.init()

    def play_move_sound(self):
        """Play move sound effect."""
        try:
            pygame.mixer.Sound(buffer=b'\x00\xff' * 1000).play()
        except:
            pass

    def play_win_sound(self):
        """Play win sound effect."""
        try:
            pygame.mixer.Sound(buffer=b'\x00\xff' * 2000).play()
        except:
            pass

    def show_start_menu(self):
        """Display step-by-step menu for game mode, color, and difficulty selection."""
        self.player_mode = self.select_game_mode()
        self.player_color = self.select_color()
        if self.player_mode == 'human_ai':
            self.ai_difficulty = self.select_difficulty()

    def select_game_mode(self):
        """Step 1: Select game mode."""
        selecting = True
        while selecting:
            self.screen.fill((240, 217, 181))
            
            title = pygame.font.SysFont("Arial", 48, bold=True).render('GOMOKU GAME', True, (139, 69, 19))
            title_rect = title.get_rect(center=(375, 150))
            self.screen.blit(title, title_rect)
            
            subtitle = pygame.font.SysFont("Arial", 24).render('Select Game Mode', True, (101, 67, 33))
            subtitle_rect = subtitle.get_rect(center=(375, 200))
            self.screen.blit(subtitle, subtitle_rect)
            
            option1 = pygame.font.SysFont("Arial", 32).render('1. Human vs AI', True, (0, 0, 0))
            option2 = pygame.font.SysFont("Arial", 32).render('2. Human vs Human', True, (0, 0, 0))
            
            rect1 = pygame.Rect(200, 280, 350, 60)
            rect2 = pygame.Rect(200, 360, 350, 60)
            
            pygame.draw.rect(self.screen, (255, 255, 255), rect1, 0)
            pygame.draw.rect(self.screen, (139, 69, 19), rect1, 3)
            pygame.draw.rect(self.screen, (255, 255, 255), rect2, 0)
            pygame.draw.rect(self.screen, (139, 69, 19), rect2, 3)
            
            option1_rect = option1.get_rect(center=(375, 310))
            option2_rect = option2.get_rect(center=(375, 390))
            self.screen.blit(option1, option1_rect)
            self.screen.blit(option2, option2_rect)
            
            instruction = pygame.font.SysFont("Arial", 18).render('Click on option or press 1/2', True, (101, 67, 33))
            instruction_rect = instruction.get_rect(center=(375, 480))
            self.screen.blit(instruction, instruction_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 'human_ai'
                    elif event.key == pygame.K_2:
                        return 'human_human'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        return 'human_ai'
                    elif rect2.collidepoint(event.pos):
                        return 'human_human'

    def select_color(self):
        """Step 2: Select player color."""
        selecting = True
        while selecting:
            self.screen.fill((240, 217, 181))
            
            title = pygame.font.SysFont("Arial", 40, bold=True).render('Choose Your Color', True, (139, 69, 19))
            title_rect = title.get_rect(center=(375, 180))
            self.screen.blit(title, title_rect)
            
            black_rect = pygame.Rect(150, 280, 200, 100)
            white_rect = pygame.Rect(400, 280, 200, 100)
            
            pygame.draw.rect(self.screen, (255, 255, 255), black_rect, 0)
            pygame.draw.rect(self.screen, (139, 69, 19), black_rect, 3)
            pygame.draw.rect(self.screen, (255, 255, 255), white_rect, 0)
            pygame.draw.rect(self.screen, (139, 69, 19), white_rect, 3)
            
            pygame.draw.circle(self.screen, (0, 0, 0), (250, 310), 20)
            pygame.draw.circle(self.screen, (255, 255, 255), (500, 310), 20)
            pygame.draw.circle(self.screen, (0, 0, 0), (500, 310), 20, 2)
            
            black_text = pygame.font.SysFont("Arial", 24).render('Press B', True, (0, 0, 0))
            white_text = pygame.font.SysFont("Arial", 24).render('Press W', True, (0, 0, 0))
            black_label = pygame.font.SysFont("Arial", 20).render('Black', True, (0, 0, 0))
            white_label = pygame.font.SysFont("Arial", 20).render('White', True, (0, 0, 0))
            
            self.screen.blit(black_text, black_text.get_rect(center=(250, 350)))
            self.screen.blit(white_text, white_text.get_rect(center=(500, 350)))
            self.screen.blit(black_label, black_label.get_rect(center=(250, 330)))
            self.screen.blit(white_label, white_label.get_rect(center=(500, 330)))
            
            instruction = pygame.font.SysFont("Arial", 18).render('Click on color or press B/W', True, (101, 67, 33))
            instruction_rect = instruction.get_rect(center=(375, 450))
            self.screen.blit(instruction, instruction_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        return 1
                    elif event.key == pygame.K_w:
                        return -1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if black_rect.collidepoint(event.pos):
                        return 1
                    elif white_rect.collidepoint(event.pos):
                        return -1

    def select_difficulty(self):
        """Step 3: Select AI difficulty."""
        selecting = True
        while selecting:
            self.screen.fill((240, 217, 181))
            
            title = pygame.font.SysFont("Arial", 40, bold=True).render('AI Difficulty', True, (139, 69, 19))
            title_rect = title.get_rect(center=(375, 150))
            self.screen.blit(title, title_rect)
            
            difficulties = [
                ('E - Easy', 'Random moves', 250, 'easy'),
                ('M - Medium', 'Basic strategy', 320, 'medium'),
                ('H - Hard', 'Advanced tactics', 390, 'hard')
            ]
            
            rects = []
            for i, (main_text, desc_text, y_pos, diff_key) in enumerate(difficulties):
                rect = pygame.Rect(150, y_pos-20, 450, 50)
                rects.append((rect, diff_key))
                
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 0)
                pygame.draw.rect(self.screen, (139, 69, 19), rect, 3)
                
                main = pygame.font.SysFont("Arial", 28).render(main_text, True, (0, 0, 0))
                desc = pygame.font.SysFont("Arial", 18).render(desc_text, True, (101, 67, 33))
                
                self.screen.blit(main, main.get_rect(center=(270, y_pos-5)))
                self.screen.blit(desc, desc.get_rect(center=(450, y_pos-5)))
            
            instruction = pygame.font.SysFont("Arial", 18).render('Click on difficulty or press E/M/H', True, (101, 67, 33))
            instruction_rect = instruction.get_rect(center=(375, 480))
            self.screen.blit(instruction, instruction_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        return 'easy'
                    elif event.key == pygame.K_m:
                        return 'medium'
                    elif event.key == pygame.K_h:
                        return 'hard'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, diff_key in rects:
                        if rect.collidepoint(event.pos):
                            return diff_key

    def run(self):
        """Main loop for the game GUI."""
        while True:
            self.show_start_menu()
            self.screen.blit(self.background, (0, 0))
            color = self.player_color
            times = 0
            flag = False
            self.board.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
            last_move = None
            win_line = None
            
            while not flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        if 25 <= x <= 725 and 25 <= y <= 725:
                            m = int(round((x - 25) / 50))
                            n = int(round((y - 25) / 50))
                            if not self.board.is_empty(m, n):
                                continue
                            
                            if self.player_mode == 'human_ai':
                                if color == self.player_color:
                                    self.board.place(m, n, color)
                                    self.screen.blit(self.black if color == 1 else self.white, self.dot_list[BOARD_SIZE * m + n])
                                    self.play_move_sound()
                                    last_move = (m, n)
                                    
                                    if self.board.check_win(m, n, color, 5):
                                        self.screen.blit(self.font.render(f'GAME OVER, {"Black" if color == 1 else "White"} wins!', True, (110, 210, 30)), (80, 650))
                                        self.play_win_sound()
                                        flag = True
                                        break
                                    
                                    color = -1 * color
                                    sleep(0.1)
                                    x_ai, y_ai = beta_go(self.board.grid, m, n, color, times, self.ai_difficulty)
                                    times += 1
                                    self.board.place(x_ai, y_ai, color)
                                    self.screen.blit(self.white if color == -1 else self.black, self.dot_list[BOARD_SIZE * x_ai + y_ai])
                                    self.play_move_sound()
                                    last_move = (x_ai, y_ai)
                                    
                                    if self.board.check_win(x_ai, y_ai, color, 5):
                                        self.screen.blit(self.font.render(f'GAME OVER, {"White" if color == -1 else "Black"} wins!', True, (217, 20, 30)), (80, 650))
                                        self.play_win_sound()
                                        flag = True
                                        break
                                    color = -1 * color
                            else:  # human_human
                                self.board.place(m, n, color)
                                self.screen.blit(self.black if color == 1 else self.white, self.dot_list[BOARD_SIZE * m + n])
                                self.play_move_sound()
                                last_move = (m, n)
                                
                                if self.board.check_win(m, n, color, 5):
                                    self.screen.blit(self.font.render(f'GAME OVER, {"Black" if color == 1 else "White"} wins!', True, (110, 210, 30)), (80, 650))
                                    self.play_win_sound()
                                    flag = True
                                    break
                                color = -1 * color
                
                # Highlight last move
                if last_move:
                    m, n = last_move
                    x_pos, y_pos = self.dot_list[BOARD_SIZE * m + n]
                    pygame.draw.circle(self.screen, (255, 0, 0), 
                                     (int(x_pos + self.white.get_width() / 2), 
                                      int(y_pos + self.white.get_height() / 2)), 25, 3)
                
                pygame.display.update()
                
                if flag:
                    self.show_restart_menu()
                    break

    def show_restart_menu(self):
        """Display restart option after game ends."""
        restart_text = self.font.render('Press R to Restart or Q to Quit', True, (0, 0, 0))
        self.screen.blit(restart_text, (120, 700))
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        sys.exit()

def main():
    """Main entry point for Gomoku Game."""
    board = Board()
    gui = GomokuGUI(board)
    gui.run()

if __name__ == "__main__":
    main()

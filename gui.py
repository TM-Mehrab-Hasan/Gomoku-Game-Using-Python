"""
Pygame GUI for Gomoku.
"""
import pygame
from pygame.locals import *
from time import sleep
from game_logic import BOARD_SIZE
from ai_logic import beta_go

BG_PATH = './GUI_Pic/bg.png'
WHITE_PATH = './GUI_Pic/white.png'
BLACK_PATH = './GUI_Pic/black.png'

MOVE_SOUND_PATH = None  # Use Pygame beep if no file
WIN_SOUND_PATH = None

class GomokuGUI:
    """
    Handles the graphical user interface for Gomoku using Pygame.
    """
    def __init__(self, board):
        """
        Initialize the GUI, load images, set up the board, and sounds.
        """
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
        self.move_sound = None
        self.win_sound = None
        if MOVE_SOUND_PATH:
            self.move_sound = pygame.mixer.Sound(MOVE_SOUND_PATH)
        if WIN_SOUND_PATH:
            self.win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)

    def play_move_sound(self):
        """Play move sound effect."""
        if self.move_sound:
            self.move_sound.play()
        else:
            pygame.mixer.Sound(buffer=pygame.sndarray.make_sound(pygame.surfarray.array2d(self.screen))).play()

    def play_win_sound(self):
        """Play win sound effect."""
        if self.win_sound:
            self.win_sound.play()
        else:
            pygame.mixer.Sound(buffer=pygame.sndarray.make_sound(pygame.surfarray.array2d(self.screen))).play()

    def show_start_menu(self):
        """Display the start menu and handle player selection, color choice, and difficulty."""
        self.screen.blit(self.background, (0, 0))
        title = self.font.render('Gomoku Game', True, (0, 0, 0))
        option1 = self.font.render('1. Human vs AI', True, (0, 0, 0))
        option2 = self.font.render('2. Human vs Human', True, (0, 0, 0))
        color_choice = self.font.render('Press B for Black, W for White', True, (0, 0, 0))
        diff_text = self.font.render('Select AI Difficulty: E=Easy, M=Medium, H=Hard', True, (0, 0, 0))
        self.screen.blit(title, (220, 200))
        self.screen.blit(option1, (220, 300))
        self.screen.blit(option2, (220, 370))
        self.screen.blit(color_choice, (120, 450))
        self.screen.blit(diff_text, (120, 520))
        pygame.display.update()
        selecting = True
        self.player_mode = None
        self.player_color = 1  # Default to Black
        self.ai_difficulty = 'medium'  # Default
        while selecting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_1:
                        self.player_mode = 'human_ai'
                    elif event.key == pygame.K_2:
                        self.player_mode = 'human_human'
                    elif event.key == pygame.K_b:
                        self.player_color = 1  # Black
                    elif event.key == pygame.K_w:
                        self.player_color = -1  # White
                    elif event.key == pygame.K_e:
                        self.ai_difficulty = 'easy'
                    elif event.key == pygame.K_m:
                        self.ai_difficulty = 'medium'
                    elif event.key == pygame.K_h:
                        self.ai_difficulty = 'hard'
                    if self.player_mode is not None:
                        selecting = False

    def run(self):
        """
        Main loop for the game GUI. Handles events, drawing, and game flow.
        """
        while True:
            self.show_start_menu()
            self.screen.blit(self.background, (0, 0))
            color = self.player_color
            times = 0
            flag = False
            self.board.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]  # Reset board
            last_move = None
            win_line = None
            while not flag:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
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
                                    win_line = self.get_win_line(m, n, color)
                                    if self.board.check_win(m, n, color, 5):
                                        self.screen.blit(self.font.render(f'GAME OVER, {"Black" if color == 1 else "White"} wins!', True, (110, 210, 30)), (80, 650))
                                        if win_line:
                                            self.draw_win_line(win_line)
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
                                    win_line = self.get_win_line(x_ai, y_ai, color)
                                    if self.board.check_win(x_ai, y_ai, color, 5):
                                        self.screen.blit(self.font.render(f'GAME OVER, {"White" if color == -1 else "Black"} wins!', True, (217, 20, 30)), (80, 650))
                                        if win_line:
                                            self.draw_win_line(win_line)
                                        self.play_win_sound()
                                        flag = True
                                        break
                                    color = -1 * color
                                else:
                                    # Ignore clicks when it's AI's turn
                                    continue
                            else:  # human_human
                                self.board.place(m, n, color)
                                self.screen.blit(self.black if color == 1 else self.white, self.dot_list[BOARD_SIZE * m + n])
                                self.play_move_sound()
                                last_move = (m, n)
                                win_line = self.get_win_line(m, n, color)
                                if self.board.check_win(m, n, color, 5):
                                    self.screen.blit(self.font.render(f'GAME OVER, {"Black" if color == 1 else "White"} wins!', True, (110, 210, 30)), (80, 650))
                                    if win_line:
                                        self.draw_win_line(win_line)
                                    self.play_win_sound()
                                    flag = True
                                    break
                                color = -1 * color
                # Highlight last move
                if last_move:
                    self.highlight_last_move(last_move)
                pygame.display.update()
                if flag:
                    self.show_restart_menu()
                    break

    def highlight_last_move(self, move):
        """Draw a red circle around the last move."""
        m, n = move
        x, y = self.dot_list[BOARD_SIZE * m + n]
        pygame.draw.circle(self.screen, (255, 0, 0), (int(x + self.white.get_width() / 2), int(y + self.white.get_height() / 2)), 25, 3)

    def get_win_line(self, x, y, color):
        """Return the coordinates of the winning line if exists."""
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            count = 1
            line = [(x, y)]
            for step in range(1, 5):
                nx, ny = x + dx*step, y + dy*step
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board.grid[nx][ny] == color:
                    line.append((nx, ny))
                    count += 1
                else:
                    break
            for step in range(1, 5):
                nx, ny = x - dx*step, y - dy*step
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board.grid[nx][ny] == color:
                    line.insert(0, (nx, ny))
                    count += 1
                else:
                    break
            if count >= 5:
                return line
        return None

    def draw_win_line(self, line):
        """Draw a green line over the winning sequence."""
        if not line or len(line) < 2:
            return
        start = self.dot_list[BOARD_SIZE * line[0][0] + line[0][1]]
        end = self.dot_list[BOARD_SIZE * line[-1][0] + line[-1][1]]
        start_pos = (int(start[0] + self.white.get_width() / 2), int(start[1] + self.white.get_height() / 2))
        end_pos = (int(end[0] + self.white.get_width() / 2), int(end[1] + self.white.get_height() / 2))
        pygame.draw.line(self.screen, (0, 255, 0), start_pos, end_pos, 6)

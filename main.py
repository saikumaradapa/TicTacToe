# TicTacToe.py
""" This is a TIC TOC TOE game from sai kumar adapa """
print("Click r to restart and ESC to stop the game")


# modules
import pygame, sys
import numpy as np
# initialisation
pygame.init()


# constants and variables
width = 600
height = 600
board_color = (28, 170, 156)
red = (255, 0, 0)
line_color = (23, 145, 135)
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cicle_color = (239, 231, 200)
cross_width = 25
cross_color = (66, 66, 66)
cross_space = 55



# screen
screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption("TIC TAC TOE game from sai kumar adapa                      (R = restart, ESC = quit)")
screen.fill(board_color)


# drawing horizontal and vertical lines
def test_box():
    pygame.draw.line(screen, red, (50,150),(150,150), 10)
    pygame.draw.line(screen, red, (50,150),(50,50), 10)
    pygame.draw.line(screen, red, (50,50),(150,50), 10)
    pygame.draw.line(screen, red, (150,150),(150,50), 10)
def draw_lines() :
    pygame.draw.line(screen, line_color, (0,200), (600, 200), 10)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), 10)
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), 10)
board = np.zeros((board_rows, board_cols))


# draw circles and cross
def draw_figures() :
    for i in range(board_rows) :
        for j in range(board_cols):
            if board[i][j] == 1:
                pygame.draw.circle(screen, cicle_color, ((int(j*200+100)), int(i*200+100)), circle_radius, circle_width)
            elif board[i][j] == 2 :
                pygame.draw.line(screen, cross_color, (j*200+cross_space, i*200+200- cross_space), (j*200+200-cross_space, i*200+cross_space), cross_width)
                pygame.draw.line(screen, cross_color, (j*200+cross_space, i*200+ cross_space), (j*200+200-cross_space, i*200+200-cross_space), cross_width)

# functions
def mark_sqaure(row, col, player) :
    board[row][col] = player

def available_square(row, col) :
    return board[row][col]==0

def is_full_board():
    for i in range(board_rows) :
        for j in range(board_cols) :
            if board[i][j] == 0:
                return False
    return True

def check_win(player) :
    # vertical
    for col in range(board_cols) :
        if board[0][col] == player and board[1][col] == player and board[2][col] == player :
            draw_vertical_winning_line(col, player)
            return True

    # horizontal
    for row in range(board_rows) :
        if board[row][0] == player and board[row][1] == player and board[row][2] == player :
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player  :
        draw_asc_diagonal(player)
        return True

    # desc diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player :
        draw_desc_diagonal(player)
        return True

    return False



# Draw winning lines
def draw_vertical_winning_line(col, player) :
    posX = col*200+100
    if player == 1 :
        color = cicle_color
    elif player == 2 :
        color = cross_color

    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)
def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = cicle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)
def draw_asc_diagonal(player):
    if player == 1:
        color = cicle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, height-15), (width - 15, 15), 15)
def draw_desc_diagonal(player):
    if player == 1:
        color = cicle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)
def restart() :

    screen.fill(board_color)
    draw_lines()
    # player = 1
    # game_over = False
    # board = np.zeros([board_rows, board_cols])
    # for row in range(board_rows) :
    #     for col in range(board_cols) :
    #         board[row][col] = 0






# mark_sqaure(1,1,1)
# print(is_full_board())

draw_lines()
# test_box()

player = 1
game_over = False


#main loop
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]


            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)


            # print(clicked_row, clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1 :
                    mark_sqaure(clicked_row, clicked_col, 1)
                    if check_win(player) :
                        game_over = True
                    player = 2

                elif player == 2 :
                    mark_sqaure(clicked_row, clicked_col, 2)
                    if check_win(player) :
                        game_over = True
                    player = 1

                draw_figures()
                #print(board)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r :
                restart()
                player = 1
                game_over = False
                print(board)
                board = np.zeros([board_rows, board_cols])
            if event.key == pygame.K_ESCAPE :
                sys.exit()


    pygame.display.update()

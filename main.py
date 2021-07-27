import sys

import pygame

pygame.init()
display = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic Tac Toe")

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def message(string, string2):
    msg = pygame.font.SysFont(None, 20).render(string, True, (255, 0, 0))
    msg2 = pygame.font.SysFont(None, 20).render(string2, True, (255, 0, 0))
    display.fill((0, 0, 0))
    display.blit(msg, [100, 150])
    display.blit(msg2, [40, 180])


def draw_grid():
    line_color = (255, 255, 255)
    for x in range(1, 3):
        # line(1. display where the lines will be displayed
        #       2. color of the lines
        #       3. starting point(x_coordinate, y_coordinate)
        #       4. end point)
        pygame.draw.line(display, line_color, (0, x * 100), (300, x * 100))
        pygame.draw.line(display, line_color, (x * 100, 0), (x * 100, 300))


def draw_marks():
    line_color = (255, 255, 255)
    x_position = 0
    for x in board:
        # y_position is the current position of the elements in the column, the list within the board list
        y_position = 0
        for y in x:
            if y == 1:
                # drawing a cross, that goes from top-left to bottom-right, and then top-right to bottom-left
                # the fifth argument is the thickness of the line
                # drawing the line from top-left to bottom-right
                pygame.draw.line(display, line_color, (x_position * 100, y_position * 100),
                                 (x_position * 100 + 100, y_position * 100 + 100), 5)
                # drawing the line from top-right to bottom-left
                pygame.draw.line(display, line_color, (x_position * 100, y_position * 100 + 100),
                                 (x_position * 100 + 100, y_position * 100), 5)
            if y == -1:
                pygame.draw.circle(display, line_color, (x_position * 100 + 50, y_position * 100 + 50), 40, 5)
            y_position += 1
        x_position += 1


def check_win():
    # column:
    if board[0][0] + board[1][0] + board[2][0] == 3:
        return 1
    if board[0][0] + board[1][0] + board[2][0] == -3:
        return 2
    if board[0][1] + board[1][1] + board[2][1] == 3:
        return 1
    if board[0][1] + board[1][1] + board[2][1] == -3:
        return 2
    if board[0][2] + board[1][2] + board[2][2] == 3:
        return 1
    if board[0][2] + board[1][2] + board[2][2] == -3:
        return 2

    # rows
    if board[0][0] + board[0][1] + board[0][2] == 3:
        return 1
    if board[0][0] + board[0][1] + board[0][2] == -3:
        return 2
    if board[1][0] + board[1][1] + board[1][2] == 3:
        return 1
    if board[1][0] + board[1][1] + board[1][2] == -3:
        return 2
    if board[2][0] + board[2][1] + board[2][2] == 3:
        return 1
    if board[1][0] + board[1][1] + board[1][2] == -3:
        return 2

    # diagonal
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
        return 1
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
        return 2

    if board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 \
            and board[1][1] != 0 and board[1][2] != 0 and board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0:
        return 3


def game_loop():
    global board
    player = 1
    run = True
    game_over = False
    while run:

        # if the game is over, user will have choice to whether continue playing or quit
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    # run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        run = False

                    # if user chooses to continue playing, then all the important variables will be reset
                    # game loop will be rerun
                    if event.key == pygame.K_p:
                        display.fill((0, 0, 0))
                        board = [
                            [0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]
                        ]
                        pygame.event.clear()
                        game_loop()
                        game_over = False

        draw_grid()
        draw_marks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if not game_over:
                if event.type == pygame.MOUSEBUTTONUP:
                    # getting the x and y coordinate of the place where mouse click event happened
                    pos = pygame.mouse.get_pos()
                    x = pos[0] // 100
                    y = pos[1] // 100

                    # getting the tile that has been clicked
                    # floor function used to determine which tile is clicked // 0, 1 or 2
                    # will alternate between player 1 and player 2, player 1 is represented by 1, and player 2 is -1
                    if board[x][y] == 0:  # beginning of the game
                        board[x][y] = player
                        player *= -1

                    if check_win() == 1 or check_win() == 2 or check_win() == 3:
                        if check_win() == 1:
                            message("Player 1 win", "press P to play again or press q to quit")
                        if check_win() == 2:
                            message("Player 2 win", "press P to play again or press q to quit")
                        if check_win() == 3:
                            message("It is a tie", "press P to play again or press q to quit")
                        game_over = True

        pygame.display.update()


game_loop()
pygame.quit()

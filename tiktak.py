
import pygame, random
from pygame.locals import (
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    MOUSEBUTTONUP
)

pygame.init()
pygame.font.init() 

#Setting colors
black = (0,0,0)


#Setting basis for screen
sh, sw = 700, 850
screen = pygame.display.set_mode([sh, sw])
pygame.display.set_caption('Tik Tak Toe')
player = random.randint(1,2)
turn = 1
a_wins, b_wins = 0, 0

comic= pygame.font.SysFont('Comic Sans MS', 30)

p1 = comic.render("It is player 1's turn", False, (0, 0, 0))
p2 = comic.render("It is player 2's turn", False, (0, 0, 0))
win1 = comic.render('Player 1 wins!', False, (0, 0, 0))
win2 = comic.render('Player 2 wins!', False, (0, 0, 0))
tie = comic.render("It's a tie! That's why this game is ass", False, (0, 0, 0))

row1 = [100, 100, 100]
row2 = [100, 100, 100]
row3 = [100, 100, 100]
board = [row1, row2, row3]

srow1 = [1,2,3]
srow2 = [4,5,6]
srow3 = [7,8,9]
sboard = [srow1, srow2, srow3]


#Function to determine which particular square the mouse is attempting to click on
def good_square(x, y):
    j = which_column(x)
    i = which_row(y)
    if i > 2 or j > 2:
        return 0
    return sboard[i][j]

def which_column(x):
    if x > 50 and x < 250:
        return 0
    elif x > 250 and x < 450:
        return 1
    elif x > 450 and x < 650:
        return 2
    else:
        return 3

def which_row(y):
    if y > 50 and y < 250:
        return 0
    elif y > 250 and y < 450:
        return 1
    elif y > 450 and y < 650:
        return 2
    else:
        return 3

#Function to place an x or o on the particular square that the player picked
def change_board(player, x, y):
    numx, numy = which_row(x), which_column(y)
    if board[numx][numy] == 100:
        if player%2 == 1:
            board[numx][numy] = 1
        else:
            board[numx][numy] = 2

def win_state(board):
    ind = 0
    for i in board:
        if (board[ind][0] + board[ind][1] + board[ind][2]) == 3 or (board[ind][0] + board[ind][1] + board[ind][2]) == 6:
            return True
        ind += 1
    ind = 0
    for i in board:
        if (board[0][ind] + board[1][ind] + board[2][ind]) == 3 or (board[0][ind] + board[1][ind] + board[2][ind]) == 6:
            return True
    if (board[0][0] + board[1][1] + board[2][2]) ==3  or (board[0][2] + board[1][1] + board[2][0]) == 6:
        return True
    elif (board[0][0] + board[1][1] + board[2][2]) == 3 or (board[0][2] + board[1][1] + board[2][0]) ==6:
        return True
    else:
        return False

#Setting up the game loops
running = True
while running:
    
    #Setting mouse position
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            if not win_state(board):
                square = good_square(mx, my)
                if square != 0:
                    change_board(player, mx, my)
                    turn += 1
                    if player == 1:
                        player = 2
                    else:
                        player = 1 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    #Setting up the physical grid
    pygame.draw.lines(screen, black, False, [(250,50), (250,650)], 5)
    pygame.draw.lines(screen, black, False, [(450,50), (450,650)], 5)

    pygame.draw.lines(screen, black, False, [(50,250), (650,250)], 5)
    pygame.draw.lines(screen, black, False, [(50,450), (650,450)], 5)

    pygame.draw.lines(screen, black, False, [(50,50), (50,650)], 5)
    pygame.draw.lines(screen, black, False, [(650,50), (650,650)], 5)
    pygame.draw.lines(screen, black, False, [(50,50), (650,50)], 5)
    pygame.draw.lines(screen, black, False, [(50,650), (650,650)], 5)

    pygame.draw.lines(screen, black, False, [(0,700), (700,700)], 10)

    ind_row = 0

    for i in board:
        ind_col = 0
        for j in i:
            if j != 100:
                if j == 1:
                    posx = 150 + (200*ind_row)
                    posy = 150 + (200*ind_col)
                    pygame.draw.circle(screen, black, (posx, posy), 90)
                    pygame.draw.circle(screen, (255,255,255), (posx, posy), 80)  
                else:
                    posx = 50 + (200*ind_row)
                    posy = 50 + (200*ind_col)
                    pygame.draw.lines(screen, black, False, [(posx,posy), (posx+200,posy+200)], 5)
                    pygame.draw.lines(screen, black, False, [(posx+200,posy), (posx,posy+200)], 5)
            ind_col += 1
        ind_row += 1

    if player == 1:
        if win_state(board):
            screen.blit(win1,(200, 725))
        elif turn >= 10:
             screen.blit(tie, (100, 725))
        else:
            screen.blit(p1,(225, 725))
    else:
        if win_state(board):
            screen.blit(win2,(200, 725))
        elif turn >= 10:
            screen.blit(tie, (100, 725))
        else:
            screen.blit(p2,(225, 725))

    pygame.display.flip()




pygame.quit()
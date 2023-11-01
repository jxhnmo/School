# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Mo, Kate Kroeger, Sophie Schneider, Maria Mercado
# Section:      516
# Assignment:   Final Project
# Date:         12/07/2022
#

# imports
import numpy as np
from math import *
import pygame
import random
import time
#from easyAI import TwoPlayersGame, id_solve, Human_Player, AI_Player
#from easyAI.AI import TT

# create colours to use
gridColour = (203, 195, 227)
whiteColour = (255, 255, 255)
redColour = (255, 114, 111)
colour2 = (173, 216, 230)
blackColour = (0, 0, 0)

# functions
def createBoard():  # creating board
    '''creates a board of zeroes'''
    board = np.zeros((6, 7))
    return board


def checkPlayer():  # check if it is single player or two player
    '''ask for user to input if single player or two player'''
    try:
        userInput = input("Single Player (1) or Two PLayer(2): ")
        if int(userInput) + 1 == 2:
            return True
        else:
            return False
    except:
        print("Invalid Input")


def placePiece(board, row, col, player):
    '''places the piece that player chooses'''
    board[row][col] = player


def validColumn(board, col):
    '''checks if the column is valid or if is maxed out'''
    return board[5, col] == 0


def positionColumn(board, col):
    '''checks for which position is empty first to put player piece'''
    for row in range(6):
        if board[row][col] == 0:
            return row


def printBoard(board):
    '''outputs board on console'''
    print(np.flip(board, 0))


def drawBoard(board):
    '''draws board in output popup'''
    for col in range(7):
        for row in range(6):
            pygame.draw.rect(screen, gridColour, (col * squareSize, (row + 1) * squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, whiteColour,
                               (int(col * squareSize + squareSize / 2), int((row + 1) * squareSize + squareSize / 2)),
                               rad)

    for col in range(7):
        for row in range(6):
            if board[row][col] == 1:
                pygame.draw.circle(screen, redColour, (
                int(col * squareSize + squareSize / 2), height - int(row * squareSize + squareSize / 2)), rad)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, colour2, (
                int(col * squareSize + squareSize / 2), height - int(row * squareSize + squareSize / 2)), rad)

    pygame.display.update()


def checkWin(board, player):
    '''runs every play to check if player has won'''
    # check vertical column for win con
    for row in range(6 - 3):  # subtract 3 to factor in the space
        for col in range(7):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and \
                    board[row + 3][col] == player:
                return True

    # check horizontal row for win con
    for row in range(6):
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and \
                    board[row][col + 3] == player:
                return True

    # check pos diagonal row for win con
    for row in range(6 - 3):  # subtract 3 to factor in the space
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and \
                    board[row + 3][col + 3] == player:
                return True

    # check neg diagonal row for win con
    for row in range(3, 6):  # start at 3 to factor in the space
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and \
                    board[row - 3][col + 3] == player:
                return True

    return False

def aiCheckConnection(board, player):
    '''runs each AI play to check if there is a 3 in a row that it can complete and win'''
    # check vertical column for 3 in a row
    for row in range(6 - 3):  # subtract 3 to factor in the space
        for col in range(7):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and \
                    board[row + 3][col] == 0:
                return col

    # check horizontal row for 3 in a row
    for row in range(6):
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player:
                if board[row][col + 3] == 0:
                    return col + 3
                else:
                    if col != 0:
                        if board[row][col - 1] == 0:
                            return col - 1

    # check pos diagonal row for 3 in a row
    for row in range(6 - 3):  # subtract 3 to factor in the space
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player:
                if board[row + 3][col + 3] == 0:
                    return col + 3
                else:
                    if row != 0 and col != 0:
                        if board[row - 1][col - 1] == 0:
                            return col - 1

    # check neg diagonal row for 3 in a row
    for row in range(3, 6):  # start at 3 to factor in the space
        for col in range(7 - 3):  # subtract 3 to factor in the space
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player:
                if board[row - 3][col + 3] == 0:
                    return col + 3
                else:
                    if row != 0 and col != 0:
                        if board[row - 1][col - 1] == 0:
                            return col - 1

    return False

def checkTie(board):
    '''check if there are still spaces'''
    if 0 in board:
        return False
    return True

# main code
# check if single player or two player
singlePlayer = checkPlayer()  # run checkPlayer

# initialising board
pygame.init()

squareSize = 100
width = 7 * squareSize
height = 7 * squareSize
size = (width, height)
rad = int(squareSize / 2 - 5)
screen = pygame.display.set_mode(size)
textFont = pygame.font.SysFont("Comic Sans", 50)
tallyFont = pygame.font.SysFont("Comic Sans", 15)
pygame.draw.rect(screen, whiteColour, (0, 0, width, squareSize))

img = pygame.image.load("prof.jpg").convert()   # getting image
profImg = pygame.transform.scale(img, (100, 100))   # resizing image


# initialise values for while loop
win = False
playAgain = True

# tally for wins
p1Wins, p2Wins = 0, 0

# gameplay
while playAgain:
    # resets board
    board = createBoard()
    printBoard(board)
    turn = 0
    drawBoard(board)
    pygame.display.update()
    playAgainChoice = False # sets val to false so that player can choose again after this game

    while not win:  # while no one has won yet, the game will keep playing
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:    # when user clicks, it will run
                #pygame.draw.rect(screen, whiteColour, (0, 0, width, squareSize))
                if turn == 0:
                    #col = int(input("Player 1: ")) - 1
                    posx = event.pos[0]
                    col = int(floor(posx / squareSize))     # calculates the closest column to user click position x

                    if validColumn(board, col): # if user column is valid it will place
                        row = positionColumn(board, col)
                        placePiece(board, row, col, 1)

                        if checkWin(board, 1):
                            win = True
                            p1Wins += 1
                            label = textFont.render("Player 1 wins", 1, redColour)
                            screen.blit(label, (40, 10))

                        printBoard(board)
                        drawBoard(board)

                        turn += 1
                        turn = turn % 2

                else:   # player 2
                    if singlePlayer == False:
                        #col = int(input("Player 2: "))
                        posx = event.pos[0]
                        col = int(floor(posx / squareSize))

                        if validColumn(board, col):
                            row = positionColumn(board, col)
                            placePiece(board, row, col, 2)

                            if checkWin(board, 2):
                                win = True
                                p2Wins += 1
                                label = textFont.render("Player 2 wins", 1, colour2)
                                screen.blit(label, (40, 10))

                            printBoard(board)
                            drawBoard(board)

                            turn += 1
                            turn = turn % 2

        if turn != 0 and singlePlayer:
            '''AI section'''
            #print("test val")
            try:
                col = aiCheckConnection(board, 2)    # see if there is a 3 in a row to win
                #print(col)
                if col == False:
                    raise ValueError()
                print("found 3 in a row and space for a fourth")
            except(ValueError, IndexError):   # otherwise random column
                col = random.randint(1, 6)

            time.sleep(1)   # pause to make it seem like it is calculating

            if validColumn(board, col):
                row = positionColumn(board, col)
                placePiece(board, row, col, 2)

                if checkWin(board, 2):
                    win = True
                    p2Wins += 1
                    label = textFont.render("Prof wins", 1, colour2)
                    screen.blit(label, (40, 10))
                    screen.blit(profImg, (300, 0))

                printBoard(board)
                drawBoard(board)

                turn += 1
                turn = turn % 2

        if checkTie(board): # check for tie
            win = True
            label = textFont.render("Tie!", 1, colour2)
            screen.blit(label, (40, 10))

    pygame.time.wait(3000)
    pygame.draw.rect(screen, whiteColour, (0, 0, width, squareSize)) # clear area

    # printing information
    label = tallyFont.render("Play again? Left to play again, Right to end", 1, redColour)
    p1WinLabel = tallyFont.render(f"Player 1 Wins: {p1Wins}", 1, blackColour)
    p2WinLabel = tallyFont.render(f"Player 2 Wins: {p2Wins}", 1, blackColour)
    screen.blit(label, (10, 5))
    screen.blit(p1WinLabel, (500, 10))
    screen.blit(p2WinLabel, (500, 50))

    while not playAgainChoice:  # while player has not chosen to play again or end, keep looping
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:    # when user clicks as a choice
                posx = event.pos[0]

                if posx > 3.5 * squareSize:   # if right side then end game
                    playAgain = False
                else:   # if click was on left side, restart game
                    pygame.draw.rect(screen, whiteColour, (0, 0, width, squareSize))
                    screen.blit(p1WinLabel, (500, 10))
                    screen.blit(p2WinLabel, (500, 50))
                    win = False

            playAgainChoice = True
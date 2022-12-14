

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8]  + ' | ' + board[9])
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5]  + ' | ' + board[6])
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2]  + ' | ' + board[3])
    print('   |   |')



def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while not (marker ==  'X' or marker == 'O'):
        marker = input("Player1: Choose X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random

def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 2 '
    else:
        return 'Player 1 '


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    #BOARD IS FULL IF RETURN TRUE
    return True


def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))

    return position


def replay():

    return input('Do you want to play again? Enter Y or N: ')


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD ,WHO'S FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')

    player_game = input('Ready to play? Y or N? ' )
    if player_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY

    while game_on:

    ### PLAYER ONE TURN
        if turn == "Player1" :
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board, player1_marker, position)
            #Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 had won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = 'Player2'

    ### PLAYER TWO TURN
        else:
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board, player2_marker, position)
            #Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 had won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break
# BREAK OUT OF THE WHILE LOOP ON replay()
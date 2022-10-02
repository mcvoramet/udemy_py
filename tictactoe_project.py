def intro_board_display():
    object = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Welcome to Tic Tac Toe Game 2 Player!")
    print(object[1]+ '|' + object[2] + '|' + object[3])
    print(object[4]+ '|' + object[5] + '|' + object[6])
    print(object[7]+ '|' + object[8] + '|' + object[9])
    print("Position key are the following above. \n")


intro_board_display()


def player_pick():
    global player1
    global player2
    choice = ['O', 'X']
    ans = input("Player 1 pick (O or X): ")
    if ans not in choice:
         print("Invalid choice only O or X!")
         player_pick()
    else:
        if ans == 'O':
            player1 = 'O'
            player2 = 'X'
        else:
            player1 = 'X'
            player2 = 'O'


player_pick()

def gameplay():
    global lst_ans
    lst_ans =[1, 2, 3, 4, 5, 6, 7, 8, 9]
    global row
    row = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global board
    board = row[1] + "|" + row[2] + "|" + row[3] + "\n" + row[4] + "|" + row[5] + "|" + row[6] + "\n" + row[7] + "|" + row[8] + "|" + row[9]
    print(board)

    while row[1] == " " or row[2] == " " or row[3] == " " or row[4] == " " or row[5] == " " or row[6] == " " or row[7] == " " or row[8] == " " or row[9] == " " :
        global ans1
        global ans2
        ans2 = ' '
        ans1 = input("Player 1 pick position(1-9): ")
        ans1 = int(ans1)
        if ans1 not in lst_ans:
            print("Invalid input only number 1-9!")
            gameplay()
        elif ans1 == ans2:
            print("Cannot choose same position as another player!")
            gameplay()
        else:
            row[ans1] = player1
            board = row[1] + "|" + row[2] + "|" + row[3] + "\n" + row[4] + "|" + row[5] + "|" + row[6] + "\n" + row[7] + "|" + row[8] + "|" + row[9]
            print(board)
            gameplay2()


def gameplay2():
    ans2 = input("Player 2 pick position(1-9): ")
    ans2 = int(ans2)
    if ans2 not in lst_ans:
        print("Invalid input only number 1-9!")
        gameplay2()
    elif ans2 == ans1:
        print("Cannot choose same position as another player!")
        gameplay2()
    else:
        row[ans2] = player2
        board = row[1] + "|" + row[2] + "|" + row[3] + "\n" + row[4] + "|" + row[5] + "|" + row[6] + "\n" + row[7] + "|" + row[8] + "|" + row[9]
        print(board)


gameplay()


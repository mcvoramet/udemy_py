def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
display(row1, row2, row3)
print("\n")


def user_choice():
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please enter a number (0-10): ")

        # Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        # Range Check
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry your number is not in range 0-10!")
                within_range = False

    return int(choice)


print(user_choice())


game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


display_game(game_list)


def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1' ,'2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice!")

    return int(choice)


position_choice()


def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list


print(replacement_choice(game_list,1))


def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N): ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False


gameon_choice()

game_on = True
game_list = [0,1,2]

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    gameon = gameon_choice()


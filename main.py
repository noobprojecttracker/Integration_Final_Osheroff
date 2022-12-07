"""
This project is a simple Tic-Tac-Toe game where two users can choose
symbols to represent their characters and duel until there is a winner or
a draw is detected
    """
__author__ = "Mark Schwartz"
# Mark Schwartz
# This is a simple Tic Tac Toe game. I draw the board with a dictionary.
# I keep track of which letter's turn
# it is by using a variable named turns. I have two functions which run every
# iteration of the loop, and terminate
# the game when a winner/draw is found. I then offer the user the ability to
# replay the game.
import time

print('Welcome to Tic Tac Toe, grab a friend and get ready to duel in this '
      'Python interpretation of the classic'
      ' game!\n')

time.sleep(3)  # I added this to give the user a brief time to read the


# welcome statement.


def print_board(spots):  # this function prints the board
    """
python function to print out the board based on which symbol is in
which spot
    :param spots:
    """
    board = f'{spots[1]} | {spots[2]} | {spots[3]}\n{spots[4]} | {spots[5]} ' \
            f'| {spots[6]}\n{spots[7]} | {spots[8]} | ' \
            f'{spots[9]}\n'
    print(board)


def integration():
    """
this function's purpose is to meet the requirements for the integration
project which I could not fit logically into my program
    """
    print('I will now explain the use of some python operators which I could '
          'not include in my game.')
    time.sleep(3)
    print('The ** operator in python is used to raise an integer or float to '
          'another integer or float.')
    print('Here is an example of that operator in use: ')
    print('3 ** 2 is equal to', 3 ** 2, '\n')
    time.sleep(5)
    print('The * operator in python completes simple multiplication. '
          'For example, 5 * 3 will print', 5 * 3, '\n')
    time.sleep(5)
    print('The operator / is used to do division in python between 2 integers '
          'or floats.')
    print('For example, the statement 5 / 2 will print', 5 / 2, '\n')
    time.sleep(5)
    print('The // operator in python is used to do floor division. It divides '
          '2 numbers and then rounds the result'
          ' down to the nearest integer.')
    print('For example, the statement 10 // 3 in python will print',
          10 // 3, '\n')
    time.sleep(5)
    print('The + operator in python is used to complete addition. For example,'
          ' the statement 5 + 1 will print',
          5 + 1, '\n')
    time.sleep(5)
    print('The - operator in python is used to complete subtraction. '
          'For example, the statement 3 - 2 will print',
          3 - 2)
    time.sleep(5)
    print('The sep= operator in python is used to add a separator between '
          'items that need to be printed. '
          'For example, the statement print(1,3,5,sep="-") will print 1-3-5')
    print(1, 3, 5, sep='-')


def find_winner(spots):  # can detect any winner on horizontal, vertical,
    """
This function finds if there is a current winner on the board
    :param spots: this parameter is the current board spots which
    I pass in
    :return:
    """
    # or diagonal spaces
    # check rows
    for i in range(3):
        row_start = 3 * i + 1
        if spots[row_start] == spots[row_start + 1] == spots[row_start + 2]:
            return True
        col_start = i + 1
        if spots[col_start] == spots[col_start + 3] == spots[col_start + 6]:
            return True
    if spots[1] == spots[5] == spots[9]:
        return True
    if spots[3] == spots[5] == spots[7]:
        return True

    return False


def find_draw(available_spots):  # I detect a draw if all spots are full
    """
this function finds whether a draw has occurred on the board
    :param available_spots: the available spots remaining
    :return:
    """
    # and no winner is found
    if not available_spots:
        return True


def wants_to_play_again():
    """

    :return:
    """
    play_again = input('Do you wanna play again?\nPress (a) to continue... '
                       '\nPress any other key to learn about'
                       ' some operators in Python!:')
    if play_again == 'a':
        print('Ok', end='\n\n')
        return True
    # else:
    #     print('\nWelcome to your introduction to Python!')
    #     return False


def create_user():
    """
this function is used to allow a new user to be created
    :return:
    """
    user = input('Enter a letter to represent your user: ')
    while len(user) > 1:  # The > operator checks to see if the left value
        # is greater than the right value
        # I have to make sure that a user's character length is not greater
        # than one, or else
        # the printing of the board will be messed up.
        print('Usernames must be 1 character long!')
        user = input('Enter a letter to represent your user: ')
    return user


def change_a_spot(a_user, spots, available_spots):
    """
this function's purpose is to let a user choose a spot on the board, and then
place their user symbol onto that spot
    :param a_user: a user symbol
    :param spots: the dictionary of spots
    :param available_spots: the array of available spots
    :return:
    """
    continue_loop = True
    while continue_loop:
        try:
            where_to_change = int(input('Choose a spot to land on: '))
            if where_to_change in available_spots:
                continue_loop = False
            elif where_to_change not in available_spots:
                print('Sorry ' + a_user + ', this spot is unavailable! '
                                          'Try again...')  # The + string
                # operator
                # concatenates two strings together
        except ValueError:
            print('That is not a spot!')

    spots[where_to_change] = a_user
    available_spots.remove(where_to_change)
    return True


def congratulate_winner(a_user):
    """
this function congratulates the winner of the match
    :param a_user:
    """
    print('Congratulations, ' * 3, a_user, 'has won')  # The * string
    # operator prints a string multiple times


def announce_draw():
    """
this function announces that a draw has been detected
    """
    print('A draw has been detected!')


def main(a_user, another_user):
    """
this main function contains the sequence of the entire program
    :param a_user:
    :param another_user:
    """
    spots = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
             9: 9}  # I draw the board with this dictionary

    available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # I track available
    # spots in this list. once a spot is chosen,
    # I remove it from this list

    turns = 0
    letter = None

    while True:

        if turns % 2 == 0 and (turns % 2 != 1):  # The % operator returns
            # the remainder after dividing two values
            letter = a_user
        elif turns % 2 != 0 or (turns % 2 == 1):
            letter = another_user

        print_board(spots)

        if change_a_spot(letter, spots, available_spots):
            turns += 1

        if find_winner(spots):
            print_board(spots)
            congratulate_winner(letter)
            break

        elif find_draw(available_spots):
            print_board(spots)
            announce_draw()
            break

    if wants_to_play_again():
        same_users = input('Do you want to use the same user symbols?: Type a '
                           'for yes or b for no: ')
        if same_users.lower() == 'a':
            main(a_user, another_user)
        else:
            user1 = create_user()
            user2 = create_user()
            while user2 == user1:
                user2 = create_user()
            main(user1, user2)
    else:
        print('Ok. Now enjoy learning about some operators in Python')
        integration()


if __name__ == '__main__':
    first_user = create_user()
    second_user = create_user()
    while second_user == first_user:
        second_user = create_user()
    main(first_user, second_user)

"""
This module contains the get_user_choice function.
Prints the menu and gets the user's choice.

    Parameters:
        None

    Returns:
        int: The user's choice
"""

def get_user_choice():
    """
    Prints the menu and gets the user's choice.
    """
    while True:
        print('1: Look up a city')
        print('2: Add a city')
        print('3: Exit')

        # get user input and validate

        choice = input('Enter your selection (1-3): ')

        if not choice.isdigit():
            print('\nInvalid selection\n')
        else:
            break

    return int(choice)
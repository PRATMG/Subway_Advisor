"""
This module contains the function get_new_state_name

    Parameters:
        None

    Returns:
        state (str): The name of a state
"""

def get_new_state_name():
    """
    Function to get the name of a state from the user
    and validate it
    """

    bad_chars = ('?', '!', '/', '\\', '@', '#', '$', '%', '^', '&', '*',
                 '(', ')', '_', '+', '=', '~', '`', '[', ']', '{', '}',
                 '|', '<', '>', ',', '.', ';', ':', '"')

    while True:
       state = input("Enter the name of the state: ")

       good_name = True
       for letter in state:
           if letter in bad_chars:
               print('State names can not contain characters such as: "/", "?" or "!"')
               good_name = False
               break

       if good_name:
           break

    return state

"""
This module contains the function get_new_city_name

    Parameters:
        None

    Returns:
        name (str): The name of a city
"""

def get_new_city_name():
    """
    Function to get the name of a city from the user
    and validate it
    """

    bad_chars = ('?', '!', '/', '\\', '@', '#', '$', '%', '^', '&', '*',
                 '(', ')', '_', '+', '=', '~', '`', '[', ']', '{', '}',
                 '|', '<', '>', ',', '.', ';', ':', '"')
    

    # get city information from the user
    while True:
        name = input('Enter "Cancel" to cancel\nEnter the name of the city: ')

        good_name = True
        for letter in name:
            if letter in bad_chars:
                print('City names can not contain characters such as: "/", "?" or "!"')
                good_name = False
                break

        if good_name:
            break
    
    return name

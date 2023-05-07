"""
This module contains the function to get the name of a country from the user
and validate it

    Parameters:
        None
        
        Returns:
            country (str): The name of a country
            
"""

def get_new_country():
    """
    Function to get the name of a country from the user
    and validate it
    """

    bad_chars = ('?', '!', '/', '\\', '@', '#', '$', '%', '^', '&', '*',
                 '(', ')', '_', '+', '=', '~', '`', '[', ']', '{', '}',
                 '|', '<', '>', ',', '.', ';', ':', '"')
    
    while True:
        country = input("Enter the full name country of the city: ")
        good_name = True
        for letter in country:
            if letter in bad_chars:
                print('City names can not contain characters such as: "/", "?" or "!"')
                good_name = False
                break

        if good_name:
            break

    return country
    
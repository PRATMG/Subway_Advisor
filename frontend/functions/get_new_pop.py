"""
This module contains the function get_new_pop

    Parameters:
        None

    Returns:
        pop (int): The population of a city
"""

def get_new_pop():
    """
    Function to get the population of a city from the user
    and validate it
    """
    
    while True:
        try:
            pop = int(input("Enter the population of the city: "))

            if pop < 0:
                print('Invalid input: Population can not be negative.')
            elif pop == 0:
                print('Invalid input: Population can not be 0.')
            else:
                break
        except ValueError:
            print("Invalid input. Population must be an integer value.\n")

    return pop
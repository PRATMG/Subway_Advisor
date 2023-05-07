"""
This module contains a function to add a city to the database.

    Parameters:
        conn (sqlite3.Connection): A connection to the database
        us_city_list (list): A list of USCity objects
        world_city_list (list): A list of WorldCity objects

    Returns:
        None

"""

from functions.add_us_city import add_us_city
from functions.add_world_city import add_world_city

def get_add_city(conn, us_city_list, world_city_list):
    """
    Adds a city to the database.
    """

    while True:
            is_us = input('Is the city in the United States?: ')

            # Ask user if the city is in the US or not
            if is_us.lower() in ('y', 'yes'):
                new_city = add_us_city(conn, us_city_list)
                if new_city is not None:
                    us_city_list.append(new_city)
                break

            elif is_us.lower() in ('n', 'no'):
                new_city = add_world_city(conn, world_city_list)
                if new_city is not None:
                    world_city_list.append(new_city)
                break

            else:
                print('\nInvalid input\n')
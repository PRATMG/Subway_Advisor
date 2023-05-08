"""
This module contains the add_us_city function, which prompts the user for information about a
new USCity and adds it to the database.

    Parameters:
        conn (Connection): Database connection object
        city_list (list): A list of USCity objects

    Returns:
        None: If the user cancels the operation
        new_city (USCity): An instance of the USCity class
"""

import sqlite3
from classes.USCity import USCity
from functions.get_new_city_name import get_new_city_name
from functions.get_new_state_name import get_new_state_name
from functions.get_new_pop import get_new_pop
from functions.get_new_area import get_new_area
from functions.get_new_growth import get_new_growth
from functions.get_next_id import get_next_id


def add_us_city(conn, city_list):
    """
     Prompts the user for information about a new USCity and adds it to the database.
    """

    is_new_city = False

    # get city information from the user
    while not is_new_city:
        name = get_new_city_name()

        if name.lower() == 'cancel':
            return None
                
        state = get_new_state_name()

        # check if the city is already in the database
        for city in city_list:
            if city.name.lower() == name.lower() and city.state.lower() == state.lower():
                print('This city is already in the database.')
                is_new_city = False
                break
            else:
                is_new_city = True

    pop = get_new_pop()
    area = get_new_area()
    density = pop / area
    growth = get_new_growth()
  

    # get the next id for the new city
    id_num = get_next_id(conn, name)

    # create a tuple of USCity to insert into the database
    city_tuple = (id_num, name, state, pop, area, density, growth, "unknown")

    query = """
        INSERT INTO us_city_class (id, name, state, population, area, population_density, growth_rate, rail_type)
        VALUES (:id, :name, :state, :population, :area, :population_density, :growth_rate, :rail_type)
    """

    # execute the query to add the new city to the us_city_class table
    while True:
        try:
            conn.execute(query, city_tuple)
            conn.commit()
            break
        except sqlite3.Error as error:
            print(f'Error adding city to the database: {error}\n')
            print('Retrying...')

    new_city = USCity(*city_tuple)

    return new_city

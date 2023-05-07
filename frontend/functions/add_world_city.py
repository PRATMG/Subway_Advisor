"""
This module contains the add_world_city function, which prompts the user for information about a
new WorldCity and adds it to the database.
"""

import sqlite3
from classes.WorldCity import WorldCity
from functions.get_new_city_name import get_new_city_name
from functions.get_new_country import get_new_country
from functions.get_new_pop import get_new_pop
from functions.get_new_area import get_new_area
from functions.get_new_growth import get_new_growth
from functions.get_next_id import get_next_id


def add_world_city(conn, city_list):
    """
     Prompts the user for information about a new WorldCity and adds it to the database.

        Parameters:
            conn (Connection): Database connection object

        Returns:
            new_city (WorldCity): An instance of the WorldCity class
    """

    is_new_city = False

    # get city information from the user
    while not is_new_city:
        name = get_new_city_name()

        if name.lower() == 'cancel':
            return None

        country = get_new_country()

        # check if the city is already in the database
        for city in city_list:
            if city.name.lower() == name.lower() and city.country.lower(
            ) == country.lower():
                print('This city is already in the database.')
                is_new_city = False
                break
            is_new_city = True

    pop = get_new_pop()
    area = get_new_area()

    density = pop / area

    growth = get_new_growth()
    id_num = get_next_id(conn, name)

    # create a tuple of WorldCity to insert into the database
    city_tuple = (id_num, name, name, country, pop, area, density, growth,
                  "unknown")

    query = """
        INSERT INTO world_city_class (id, name, name2, country, population, area, population_density, growth_rate, rail_type)
        VALUES (:id, :name, :name2, :country, :population, :area, :population_density, :growth_rate, :rail_type)
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

    new_city = WorldCity(*city_tuple)

    return new_city

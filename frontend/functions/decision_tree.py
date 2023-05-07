"""
This module contains the decision_tree function, which determines whether or not a city
is a good candidate for SubTerrain.

    Parameters:
        city (City): A City object
        min_max_tuple (tuple): A tuple containing the min and max values for the population,
        area, and population density

    Returns:
        decision (str): A string containing the decision for the city
"""

from frontend.models import UsCityClass, WorldCityClass
from .normalize_data import normalize_data


def decision_tree(city, min_max_tuple):
    """
    Receives a City object and a tuple containing the min and max values for the population,
    area, and population density.
    """
    decision = ''

    rail_type = city.rail_type.lower()

    if city.rail_type.lower() == 'subway':
        decision = f'The city of {city.name} has a subway system. You should approach the '\
                   + 'city government to offer SubServe to them.\n'

    elif rail_type != 'unknown':
        decision = f'The city of {city.name} does not have a subway, but it does have a '\
                   + f'{city.rail_type} system. It is not recommended to approach the city '\
                   + 'government.\n'

    elif isinstance(city, UsCityClass) and int(city.population) < 450000:
        decision = f'The population of {city.name} is too small to be a good candidate. It is '\
                   + 'not recommended to approach the city government.\n'

    elif isinstance(city, WorldCityClass) and city.population < 1000000:
        decision = f'The population of {city.name} is too small to be a good candidate. It is '\
                   + 'not recommended to approach the city government.\n'

    else:
        # get a rating for the city based on the population, area, and population density
        weights = [.1, .5, .3, .1]
        normalized_data = normalize_data(min_max_tuple, city)
        rating = (normalized_data[0] * weights[0]) + (normalized_data[1] * weights[1])\
           + (normalized_data[2] * weights[2]) + (normalized_data[3] * weights[3])

        rating = rating * 100

        if rating >= 80:
            decision = f'The rating for {city.name} is {rating:.2f}%, '\
                       + 'making it a great choice for SubTerrain.\n'

        elif rating >= 60:
            decision = f'The rating for {city.name} is {rating:.2f}%, '\
                       + 'making it a good choice for SubTerrain.\n'

        else:
            decision = f'The rating for {city.name} is {rating:.2f}%, '\
                       + 'making it a bad choice for SubTerrain.\n'

    return decision

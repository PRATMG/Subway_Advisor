"""
This module contains the CityClass class.

    Attributes:
        id (int): The id of the city
        name (str): The name of the city
        population (int): The population of the city
        area (float): The area of the city in square miles
        population_density (float): The population density of the city
        growth_rate (float): The population growth rate of the city
        rail_type (str): The type of rail system in the city

    Methods:
        None

    This is a parent class for the WorldCityClass and USCityClass classes.
"""

class CityClass:
    """
    Class to represent a city
    """

    def __init__(self, id_num, name, population, area, population_density,
                 growth_rate, rail_type):
        """
        The constructor for the CityClass class.
        """
        self.id = id_num
        self.name = name
        self.population = population
        self.area = area
        self.population_density = population_density
        self.growth_rate = 0.0 if growth_rate == "Unknown" else float(
            growth_rate)
        self.rail_type = rail_type

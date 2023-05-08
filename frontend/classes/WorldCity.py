"""
This module contains the WorldCity class that inherits from CityClass.

    Attributes:
        id (int): The id of the city
        name (str): The name of the city
        name2 (str): The alternate name of the city
        country (str): The country the city is in
        population (int): The population of the city
        area (float): The area of the city in square miles
        population_density (float): The population density of the city
        growth_rate (float): The population growth rate of the city
        rail_type (str): The type of rail system in the city

    Methods:
        None
"""

from classes.CityClass import CityClass


class WorldCity(CityClass):
    """
    Class to represent a city in the world
    """

    def __init__(self, id_num, name, name2, country, population, area,
                 population_density, growth_rate, rail_type):
        """
        Constructor for the WorldCity class.
        """
        super().__init__(id_num, name, population, area, population_density,
                         growth_rate, rail_type)
        self.name2 = name2
        self.country = country

    def __del__(self):
        """
        Destructor for the WorldCity class.
        """
        del self.id
        del self.name
        del self.name2
        del self.country
        del self.population
        del self.area
        del self.population_density
        del self.growth_rate
        del self.rail_type

    def __str__(self):
        """
        String representation of the WorldCity class
        """
        return f'ID: {self.id}\nName: {self.name}\nName2: {self.name2}\ncountry: {self.country}\nPopulation: {self.population}'\
                      + f'\nArea: {self.area}\nPopulation Density: {self.population_density}\nGrowth Rate: {self.growth_rate}'\
                      + f'\nRail Type: {self.rail_type}'

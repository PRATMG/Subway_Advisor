"""
This module contains the class USCity that inherits from CityClass.

    Attributes:
        id (int): The id of the city
        name (str): The name of the city
        state (str): The state the city is in
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


class USCity(CityClass):
    """
    Class to represent a city in the United States
    """

    def __init__(self, id_num, name, state, population, area, population_density,
                 growth_rate, rail_type):
        """
        Constructor for the USCity class.
        """
        super().__init__(id_num, name, population, area, population_density,
                         growth_rate, rail_type)
        self.state = state
        self.country = "United States"

    def __del__(self):
        """
        Destructor for the USCity class.
        """
        del self.id
        del self.name
        del self.state
        del self.country
        del self.population
        del self.area
        del self.population_density
        del self.growth_rate
        del self.rail_type

    def __str__(self):
        """
        String representation of the USCity class.
        """
        return f'ID: {self.id}\nName: {self.name}\nState: {self.state}\nCountry: {self.country}\
                \nPopulation: {self.population}\nArea: {self.area}\nPopulation Density: {self.population_density}\
                \nGrowth Rate: {self.growth_rate}\nRail Type: {self.rail_type}'

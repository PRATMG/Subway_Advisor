"""
This module contains the CityGrowth class.

    Attributes:
        id (int): The id of the city
        city (str): The name of the city
        state (str): The state the city is in
        country (str): The country the city is in
        growth_rate (float): The population growth rate of the city

    Methods:
        None
"""


class CityGrowth:
    """
    This class is used to store the data from the city_growth table in the database.
    """

    def __init__(self, id_num, city, state, country, growth_rate):
        """
        The constructor for the CityGrowth class.
        """
        self.id = id_num
        self.city = city
        self.state = state
        self.country = country
        self.growth_rate = growth_rate

    def __del__(self):
        """
        The destructor for the CityGrowth class.
        """
        del self.id
        del self.city
        del self.state
        del self.country
        del self.growth_rate

    def __str__(self):
        """
        The string representation of the CityGrowth class.
        """
        return f'ID: {self.id}\nCity: {self.city}\nState: {self.state}\nCountry: {self.country}'\
               + f'\nGrowth Rate: {self.growth_rate}'

"""
This module contains the class MetroCity that represents a city with a subway system.

    Attributes:
        id (int): The id of the city
        city (str): The name of the city
        name (str): The name of the city
        country (str): The country the city is in
        rail_type (str): The type of rail system in the city

    Methods:
        None
    
"""

class MetroCity:
    """
    Class to represent a city with a subway system
    """

    def __init__(self, id_num, city, name, country, rail_type):
        """
        The constructor for the MetroCity class.
        """
        self.id = id_num
        self.city = city
        self.name = name
        self.country = country
        self.rail_type = rail_type

    def __del__(self):
        """
        The destructor for the MetroCity class.
        """
        del self.id
        del self.city
        del self.name
        del self.country
        del self.rail_type
        
    def __str__(self):
        """
        The string representation of the MetroCity class.
        """
        return f'ID: {self.id}\nName: {self.name}\nCity: {self.city}\nCountry: {self.country}'\
               + f'\nRail Type: {self.rail_type}'
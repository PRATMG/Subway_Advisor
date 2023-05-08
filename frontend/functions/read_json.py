"""
This module contains the function read_json() that returns the contents of a json file.

    Parameters:
        file_name (str): The name of the file

    Returns:
        dict: The contents of the json file
"""

import json

def read_json(file_name):
    """
    Read and return the contents of a json file
    """
    with open(file_name, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

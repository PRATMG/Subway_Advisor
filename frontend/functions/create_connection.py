"""
This module contains the create_connection function, which creates a connection to the database.

    Parameters:
        database (str): The path to the database

    Returns:
        conn (Connection): Database connection object
"""

import sqlite3

# function to create a connection to the database
def create_connection(database):
    """
    Receives a path to a database and returns a connection to that database.
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as error:
        print(error)
    return conn

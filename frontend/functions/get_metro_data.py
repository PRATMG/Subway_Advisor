"""
This module contains the function get_metro_data() that returns data from the growth table.

    Parameters:
        conn (sqlite3.Connection): A connection to the database

    Returns:
        list: A list of tuples containing the data from the growth table
"""

def get_metro_data(conn):
    """
    Use the connection to execute a SQL query that returns data from the metro_systems table.
    
    """

    query = """
        SELECT
            id,
            city,
            name,
            country_region AS country,
            rail_type
           
        FROM
            metro_systems
    """

    # Execute the query and fetch the results
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

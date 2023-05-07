"""
This module contains the function get_us_city_data() that returns data from the us_city_table.

    Parameters:
        conn (sqlite3.Connection): A connection to the database

    Returns:
        list: A list of tuples containing the data from the us_city_table
"""

def get_us_city_data(conn):
    """
    Use the connection to execute a SQL query that returns data from the us_city_table.
    City from the us_cities table
    growthRate from the growth table
    rail_type from the metro_systems table

    Population density is calculated by dividing the population by the area.
    if the city is not in the growth table, the growthRate should be 'Unknown'
    if the city is not in the metro_systems table, the rail_type should be 'Unknown'
    """

    query = """
        SELECT
            id,
            name,
            state,
            population,
            area,
            population_density,
            growth_rate,
            rail_type
        FROM
            us_city_class
    """

    # Execute the query and fetch the results
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

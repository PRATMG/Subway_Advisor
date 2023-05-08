"""
This module contains the function get_growth_data() that returns data from the growth table.

    Parameters:
        conn (sqlite3.Connection): A connection to the database

    Returns:
        list: A list of tuples containing the data from the growth table
"""

def get_growth_data(conn):
    """
    Use the connection to execute a SQL query that returns data from the growth table.
    
    """

    query = """
        SELECT
            id,
            city,
            state,
            country,
            growthRate as growth_rate
           
        FROM
            growth
    """

    # Execute the query and fetch the results
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
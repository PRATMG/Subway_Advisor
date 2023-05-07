"""
This module contains the function get_next_id() that returns the next available id for a city.

    Parameters:
        conn (sqlite3.Connection): A connection to the database
        city_name (str): The name of the city
        state (str): The state of the city (default is None)

    Returns:
        int: The next available id for a city

"""


def get_next_id(conn, city_name, state=None):
    """
    Function to find the next available id for a city.
    """
    # Define the table names
    tables = ['us_city_class', 'world_city_class', 'growth', 'metro_systems']

    # List to store all ids
    ids = []

    cursor = conn.cursor()

    # Loop through the table names
    for table in tables:
        # Check if the current table has a 'state' column
        if table == 'us_city_class':
            # If found, query the id using 'name' column and 'state' column
            query = f'SELECT id FROM {table} WHERE name = ? AND state = ?'
            cursor.execute(query, (city_name, state))
        elif table == 'growth':
            # If found, query the id using 'name' column and 'state' column
            query = f'SELECT id FROM {table} WHERE city = ? AND state = ?'
            cursor.execute(query, (city_name, state))
        else:
            # Otherwise, query the id using 'city' column for 'metro_systems' table
            if table == 'metro_systems':
                query = f'SELECT id FROM {table} WHERE city = ?'
            # Query the id using 'name' column for 'world_cities' table
            else:
                query = f'SELECT id FROM {table} WHERE name = ?'
            cursor.execute(query, (city_name, ))

        # Fetch the result of the query
        result = cursor.fetchone()

        # If there's a result, return the id
        #if result:
            #return result[0]
        #else:
            #If not, collect all ids from the current table
        query = f'SELECT id FROM {table}'
        cursor.execute(query)
        ids.extend([record[0] for record in cursor.fetchall()])

    # Remove duplicates, sort the list, and check for gaps
    sorted_ids = sorted(list(set(ids)))
    for i, id_num in enumerate(sorted_ids, start=1):
        # If there's a gap, return the missing id
        if id_num != i:
            return i

    # If no gap, return the next available id
    return max(sorted_ids) + 1

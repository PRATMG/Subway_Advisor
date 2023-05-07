"""
This module contains the function get_table_count() that returns the number of rows in a table.

    Use:
        Primarily used in testing to verify that the data was loaded correctly.

    Parameters:
        conn (sqlite3.Connection): A connection to the database
        table_name (str): The name of the table

    Returns:
        int: The number of rows in the table


"""

def get_table_count(conn, table_name):
    """
    Function to find the number of rows in a table.
    """

    # return the number of rows in the table
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

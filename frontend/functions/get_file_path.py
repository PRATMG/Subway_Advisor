"""
This module contains a function to get the path to a file in the files directory.

  Parameters:
    file_name (str): The name of the file

  Returns:
    str: The path to the file

"""

import os

def get_file_path(file_name):
    """
      Get the path to a file in the files directory.
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, '..', 'files', file_name)

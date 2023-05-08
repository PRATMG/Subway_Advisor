"""
This module contains the function normalize_data() that returns normalized data.

    Parameters:
        min_max_data (tuple): A tuple containing the min and max values for each column
        this_city (City): A City object

    Returns:
        tuple: A tuple containing the normalized values for population, area,
        population density, and population growth
"""
def normalize_data(min_max_data, this_city):
    """
    Function to normalize data
    order of data in tuple: 
    [0] = min_pop
    [1] = max_pop
    [2] = min_area
    [3] = max_area
    [4] = min_pop_density
    [5] = max_pop_density
    [6] = min_pop_growth
    [7] = max_pop_growth
    
    """

    # normalize the data
    # tuple of normalized values
    normalized_city_pop = ((this_city.population - min_max_data[0]) /
                           (min_max_data[1] - min_max_data[0]))

    normalized_city_area = ((this_city.area - min_max_data[2]) /
                            (min_max_data[3] - min_max_data[2]))

    normalized_city_pop_density = ((this_city.population_density - min_max_data[4]) /
                                   (min_max_data[5] - min_max_data[4]))

    normalized_city_pop_growth = ((this_city.growth_rate - min_max_data[6]) /
                                  (min_max_data[7] - min_max_data[6]))

    normalized_values = (normalized_city_pop, normalized_city_area,
                         normalized_city_pop_density, normalized_city_pop_growth)

    return normalized_values

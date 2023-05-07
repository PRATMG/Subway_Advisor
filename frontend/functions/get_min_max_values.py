"""
The module contains a function to get the min/max values for data normalization.

  Parameters:
    city_list (list): A list of City objects

  Returns:
    tuple: A tuple containing the min/max values for population, area, 
    population density, and population growth
"""

def get_min_max_values(city_list):
    """
    Function to get the min/max values for data normalization.
    """
    max_pop = 0  # impossible to have a negative population
    min_pop = 2**63 - 1  # max value for a 64-bit integer
    max_area = 0  # impossible to have a negative area
    min_area = 9999999.0  # arbitrary large number
    max_pop_density = 0  # impossible to have a negative population density
    min_pop_density = 9999999.0  # arbitrary large number
    max_pop_growth = -9999999.0  # arbitrary small number
    min_pop_growth = 9999999.0  # arbitrary large number

    for city in city_list:
        if city.rail_type != "Unknown":

            if city.population > max_pop:
                max_pop = city.population

            if city.population < min_pop:
                min_pop = city.population

            if city.area > max_area:
                max_area = city.area

            if city.area < min_area:
                min_area = city.area

            if city.population_density > max_pop_density:
                max_pop_density = city.population_density

            if city.population_density < min_pop_density:
                min_pop_density = city.population_density

            if float(city.growth_rate) > float(max_pop_growth):
                max_pop_growth = city.growth_rate

            if float(city.growth_rate) < float(min_pop_growth):
                min_pop_growth = city.growth_rate

    min_max_tuple = (min_pop, max_pop, min_area, max_area, min_pop_density,
                     max_pop_density, min_pop_growth, max_pop_growth)

    return min_max_tuple

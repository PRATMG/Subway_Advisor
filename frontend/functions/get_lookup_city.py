"""
This module contains a function to look up a city in the database and display the results.

    Parameters:
        us_city_list (list): A list of USCity objects
        world_city_list (list): A list of WorldCity objects
        us_min_max (dict): A dictionary containing the min/max values for US cities
        world_min_max (dict): A dictionary containing the min/max values for world cities

    Returns:
        None
"""


from functions.decision_tree import decision_tree

def get_lookup_city(us_city_list, world_city_list, us_min_max, world_min_max):
    temp_city = None
    """
    Look up a city in the database and display the results.
    """
    while True:
        look_up_city = input(
            'Enter the name of the city you would like to look up: ')

        if look_up_city.isdigit():
            print('Invalid input. City names should be alpha only')

        elif look_up_city == "Washington":
            while True:
                answer = input(
                        'Are you wanting to search for Washington, D.C.?: ').lower()

                if answer in ('y', 'yes'):
                    look_up_city = "Washington, D.C."

                elif answer in ('n', 'no'):
                    break
                else:
                    print('Invalid option, please enter Y/N or Yes/No: ')

        else:
            break

    city_found = False
    results = ''
    # Look up the city in the US city list
    for city in us_city_list:
        lower_city = city.name.lower()
        if look_up_city.lower() == lower_city:
            temp_city = city
            results = decision_tree(city, us_min_max)
            city_found = True
            print(f'\n{city}\n\n{results}')
            break
    # If not found, look up the city in the world city list
    if not city_found:
        for city in world_city_list:
            lower_city = city.name.lower()
            lower_city2 = city.name2.lower()
            if look_up_city.lower() == lower_city or look_up_city.lower(
            ) == lower_city2:
                temp_city = city
                results = decision_tree(city, world_min_max)
                city_found = True
                print(f'\n{city}\n\n{results}')
                break

    # If not found, let the user know
    if not city_found:
        print(
            'The city was not found in the database, you should think about adding it.'
             )
    else:
        # Let the user try different population values
        while True:
            # Get temp data to test the city with a different population
            response = input(
            'Would you like to test the city with a different population?: ')

            if response.lower() in ('y', 'yes'):
                while True:
                    temp_pop = input('Enter the new population: ')

                    if not temp_pop.isdigit():
                        print('Invalid input, population should be numeric')
                    else:
                        temp_city.population = int(temp_pop)
                        break

                results = decision_tree(temp_city, us_min_max)
                print(f'\n{city}\n\n{results}')

            elif response.lower() in ('n', 'no'):
                if temp_city is not None:
                    del temp_city
                break

            else:
                print('Invalid input, please enter Y/N or Yes/No.')

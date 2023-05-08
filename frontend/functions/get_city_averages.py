def get_city_averages(city_list):
    # get the average population, area, population density, and growth rate of all cities in the list
    # return the averages in a tuple
    pop = 0
    area = 0
    pop_density = 0
    growth_rate = 0
    count = 0
    for city in city_list:
        pop += float(city.population)
        area += float(city.area)
        pop_density += float(city.population_density)
        if city.growth_rate != "Unknown" and city.growth_rate != "unknown":
            growth_rate += float(city.growth_rate)
            count += 1

    avg_pop = pop / len(city_list)
    avg_area = area / len(city_list)
    avg_pop_density = pop_density / len(city_list)

    # returns the avg growth rate of all cities with a known growth rate
    avg_growth_rate = growth_rate / count

    return (avg_pop, avg_area, avg_pop_density, avg_growth_rate)
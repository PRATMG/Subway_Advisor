from django.shortcuts import render
from .models import UsCityClass, WorldCityClass, MetroSystems
from .forms import UsCityForm, WorldCityForm
from .functions import decision_tree, get_min_max_values
from django.http import JsonResponse
from .functions.get_min_max_values import get_min_max_values
from .functions.decision_tree import decision_tree

def index(request):
    return render(request, 'frontend/index.html', {})

def bout(request):
    return render(request, 'frontend/bout.html', {})

def search(request):
    return render(request, 'frontend/search.html', {
    })

# def get_decision(request, city_name):
#     # Retrieve all city records
#     us_cities = UsCityClass.objects.all()
#     world_cities = WorldCityClass.objects.all()
#     cities = list(us_cities) + list(world_cities)

#     # Get the min and max values for the required fields using the get_min_max_values function
#     min_max_tuple = get_min_max_values(cities)

#     # Find the city with the given name
#     city = None
#     for c in cities:
#         if c.name.lower() == city_name.lower():
#             city = c
#             break

#     if city is None:
#         return JsonResponse({"error": "City not found"})

#     decision = decision_tree(city, min_max_tuple)
#     return JsonResponse({"decision": decision})

def get_decision(request, city_name):
    new_population = request.GET.get('new_population', None)

    # Retrieve all city records
    us_cities = UsCityClass.objects.all()
    world_cities = WorldCityClass.objects.all()
    cities = list(us_cities) + list(world_cities)

    # Get the min and max values for the required fields using the get_min_max_values function
    min_max_tuple = get_min_max_values(cities)

    # Find the city with the given name
    city = None
    for c in cities:
        if c.name.lower() == city_name.lower():
            city = c
            break

    if city is None:
        return JsonResponse({"error": "City not found"})

    if new_population:
        # If new_population is provided, update the city population and population_density
        city.population = int(new_population)
        city.population_density = city.population / city.area

    decision = decision_tree(city, min_max_tuple)
    return JsonResponse({"decision": decision})




def city_data(request):
    # Retrieve all city records
    us_cities = UsCityClass.objects.all()
    world_cities = WorldCityClass.objects.all()
    cities = list(us_cities) + list(world_cities)

    # Convert city records to GeoJSON format
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [city.longitude, city.latitude],
                },
                "properties": {
                    "id": city.id,
                    "name": city.name,
                    "state": city.state if hasattr(city, "state") else city.name2,
                    "country": "United States" if isinstance(city, UsCityClass) else city.country,
                    "countryCode": "US" if isinstance(city, UsCityClass) else city.countrycode,
                    "population": city.population,
                    "area": city.area,
                },
            }
            for city in cities
        ],
    }

    return JsonResponse(geojson_data)

def metro_data(request):
    metro_systems = MetroSystems.objects.all()
    metro_data = [
        {
            'name': metro.name,
            'country_region': metro.country_region,
            'service_opened': metro.service_opened,
            'last_expanded': metro.last_expanded,
            'stations': metro.stations,
            'system_length': metro.system_length,
            'annual_ridership': metro.annual_ridership,
            'rail_type': metro.rail_type,
            'city_id': metro.id,
            'country': metro.country_region,
        }
        for metro in metro_systems
    ]
    return JsonResponse(metro_data, safe=False)


def UScity_add(request):
    success = False
    if request.method == 'POST':
        form = UsCityForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_state = form.cleaned_data['state']
            new_population = form.cleaned_data['population']
            new_area = form.cleaned_data['area']
            new_population_density = form.cleaned_data['population_density']
            new_growth_rate = form.cleaned_data['growth_rate']
            new_rail_type = form.cleaned_data['rail_type']            
            new_latitude = form.cleaned_data['latitude']
            new_longitude = form.cleaned_data['longitude']
            new_UsCityClass = UsCityClass(
                name = new_name,
                state = new_state,
                population = new_population,
                area = new_area,
                latitude = new_latitude,
                longitude = new_longitude,
                population_density = new_population_density,
                growth_rate = new_growth_rate,
                rail_type = new_rail_type
            )
            new_UsCityClass.save()
            success = True
    else:
        form = UsCityForm()

    context = {
        'form': form,
        'success': success,
        'cities': UsCityClass.objects.all(),
    }
    return render(request, 'frontend/uscity_add.html', context)



def Worldcity_add(request):
    success = False
    if request.method == 'POST':
        form_2 = WorldCityForm(request.POST) 
        if form_2.is_valid():
            # Check if a city with the same name and country already exists
            name = form_2.cleaned_data['name']
            country = form_2.cleaned_data['country']
            existing_city = WorldCityClass.objects.filter(name__iexact=name, country__iexact=country)

            if not existing_city.exists():
                new_WorldCityClass = form_2.save(commit=False)
                new_WorldCityClass.name2 = new_WorldCityClass.name
                new_WorldCityClass.save()
                success = True
            else:
                # You can pass an error message to the template to inform the user that the city already exists
                form_2.add_error(None, "A city with this name and country already exists.")
    else:
        form_2 = WorldCityForm()
    context = {
        'form_2': form_2,
        'success': success,
        'world_cities': WorldCityClass.objects.all(),
    }
    return render(request, 'frontend/worldcity_add.html', context)

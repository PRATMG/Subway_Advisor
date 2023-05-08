from django import forms
from .models import UsCityClass, WorldCityClass
from django.core.exceptions import ValidationError



class UsCityForm(forms.ModelForm):
    class Meta:
        model = UsCityClass
        fields = ['name', 'state', 'population', 'area','latitude', 'longitude', 'population_density', 'growth_rate', 'rail_type']
        labels = {
            'name': 'City Name',
            'state': 'State',
            'population': 'Population', 
            'area': 'Area (sq.km)', 
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'population_density': 'Population Density', 
            'growth_rate': 'Growth Rate', 
            'rail_type': 'Rail Type'
        }        

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'oninput': 'checkCityName()'}),
            'state':forms.TextInput(attrs={'class': 'form-control'}),
            'population':forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'oninput': 'updatePopulationDensity()'}), 
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'oninput': 'updatePopulationDensity()'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}), 
            'population_density': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'growth_rate': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}), 
            'rail_type':forms.TextInput(attrs={'class': 'form-control'})
        }


class WorldCityForm(forms.ModelForm):
    class Meta:
        model = WorldCityClass
        fields = ['name', 'name2', 'country', 'population', 'area', 'countrycode', 'latitude', 'longitude', 'population_density', 'growth_rate', 'rail_type']
        labels = {
            'name': 'City Name',
            'name2':'Name 2 (if any) or put same as above',
            'country': 'Country',
            'population': 'Population', 
            'area': 'Area (sq.km)',
            'countrycode': '2 letter Country abbreviation',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'population_density': 'Population Density', 
            'growth_rate': 'Growth Rate', 
            'rail_type': 'Rail Type'
        }   

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'oninput': 'checkCityNameAndCountry()'}),
            'name2': forms.TextInput(attrs={'class': 'form-control'}),           
            'country': forms.TextInput(attrs={'class': 'form-control', 'oninput': 'checkCityNameAndCountry()'}),
            'population':forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'oninput': 'updatePopulationDensity()'}), 
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'oninput': 'updatePopulationDensity()'}),
            'countrycode': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'population_density': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'growth_rate': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}), 
            'rail_type':forms.TextInput(attrs={'class': 'form-control'})

        }
from django.db import models

# Create your models here.
class Growth(models.Model):
    pop2023 = models.IntegerField()
    pop2022 = models.IntegerField()
    city = models.TextField()
    country = models.TextField()
    growthrate = models.FloatField(db_column='growthRate')  # Field name made lowercase.
    type = models.TextField()
    rank = models.IntegerField()
    state = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'growth'


class MetroSystems(models.Model):
    city = models.TextField()
    country_region = models.TextField()
    name = models.TextField()
    service_opened = models.IntegerField()
    last_expanded = models.IntegerField()
    stations = models.IntegerField()
    system_length = models.FloatField()
    annual_ridership = models.FloatField(blank=True, null=True)
    rail_type = models.TextField()

    class Meta:
        db_table = 'metro_systems'


class UsCityClass(models.Model):
    name = models.TextField()
    state = models.TextField()
    population = models.IntegerField()
    area = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()    
    population_density = models.FloatField()
    growth_rate = models.FloatField()
    rail_type = models.TextField()
    
    def __str__(self):
        return f'UsCityClass: {self.name} {self.state}'    
    
    class Meta:
        db_table = 'us_city_class'

class WorldCityClass(models.Model):
    name = models.TextField()
    name2 = models.TextField()
    country = models.TextField()
    population = models.IntegerField()
    area = models.FloatField()
    countrycode = models.TextField(db_column='countryCode')  # Field name made lowercase.
    latitude = models.FloatField()
    longitude = models.FloatField()    
    population_density = models.FloatField()
    growth_rate = models.FloatField()
    rail_type = models.TextField()

    def __str__(self):
        return f'WorldCityClass: {self.name} {self.country}'

    class Meta:
        db_table = 'world_city_class'




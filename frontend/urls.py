from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Uscity_add/',views.UScity_add, name="Uscity_add"),
    path('Worldcity_add/',views.Worldcity_add, name="Worldcity_add"),
    path('bout/',views.bout, name="bout"),
    path('search/',views.search, name="search"),
    path('metro_data/', views.metro_data, name='metro_data'),
    path('city_data/', views.city_data, name='city_data'),
    path('get_decision/<str:city_name>/', views.get_decision, name='get_decision'),

]



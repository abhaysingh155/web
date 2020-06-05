from django.urls import path
from . import views
from .views import ChartData, NameData
urlpatterns = [
    path('',views.index, name="index"),
    path('make_graph/<str:pk_country>/',views.make_graph, name="make_graph"),
    path('list_of_countries/',views.list_of_countries, name="list_of_countries"),
    path('model_form_upload/<str:pk_country>/',views.model_form_upload, name="model_form_upload"),
    path('home/', views.home, name='home'),
    path('countries/', views.countries, name='countries'),
    path('chart_data/<str:pk_country>/', ChartData.as_view(), name="ChartData"),
    path('india_home/', views.india_home, name="india_home"),
    path('name_data/', NameData.as_view(), name="NameData"),
    path('home_data/', views.home_data, name="home_data"),
    path('home_global', views.home_global, name="home_global"),
]

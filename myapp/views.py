from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import csv
import random
from django.contrib import messages
import datetime
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone


# Create your views here.
direct_links=["India","Italy"]

class NameData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		name=CountriesName.objects.values("name")
		total= name.count()
		name = [i["name"] for i in name]
		# print("name-------> ",name)
		#context={"name":name}
		return Response(name)


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, pk_country, format=None):
		get_data = CountriesData.objects.filter(country_name=pk_country)
		x_axis = [i['updated_at'].strftime("%d %b %Y <br> %H:%M:%S") for i in get_data.values()]
		today_confirmed_series = [int(i['today_confirmed']) for i in get_data.values()]
		total_deaths_series = [int(i['total_deaths']) for i in get_data.values()]
		total_recovered_series = [int(i['total_recovered']) for i in get_data.values()]
		data={ 
		"x_axis" : x_axis,
		"today_confirmed_series": today_confirmed_series,
		"total_deaths_series": total_deaths_series,
		"total_recovered_series": total_recovered_series,
		}
		return Response(data)

def index(request):
	data_dict={}
	country_1 = CountriesName.objects.values()
	for v in country_1:
		for i in CountriesData.objects.filter(country_name=v["name"]).order_by('-updated_at').values():
			data_dict.update({v["name"]:[v["name"], v["alpha3Code"], i["total_confirmed"],]})
			break

	world_data = WorldData.objects.all().order_by('-worlddata_updated_at').values()
	total_confirmed = world_data.values()[0]["worlddata_total_confirmed"]
	total_recovered = world_data.values()[0]["worlddata_total_recovered"]    
	total_deaths = world_data.values()[0]["worlddata_total_deaths"]
	today_confirmed = world_data.values()[0]["worlddata_today_confirmed"]
	return render(request, "mysite/message_buttons.html",{"D":data_dict,
														  "world_data":world_data, 
														  "total_confirmed":total_confirmed, 
														  "total_recovered":total_recovered, 
														  "total_deaths":total_deaths, 
														  "today_confirmed": today_confirmed,
														  "direct_links":direct_links,
														  })

def home_data(request):
	response = requests.get('https://restcountries.eu/rest/v2/all')
	geodata = response.json()
	print("geodata----------------->",geodata) 
	for value in geodata:
		obj,created=CountriesName.objects.get_or_create(
		name = value["name"],
		country_pic = value["flag"],
		alpha3Code =  value["alpha3Code"]
		)
		print("geodata----------------->",created)
	return render(request, "mysite/index.html")

def india_home(request):
	response = requests.get('https://api.covid19india.org/data.json')
	geodata = response.json()
	geodata = geodata["statewise"]
	for value in geodata:
		obj,created=StateData.objects.get_or_create(
			active = value["active"],
			confirmed = value["confirmed"],
			deaths = value["deaths"],
			state = value["state"],
			updated_on = timezone.now()
			)
	return render(request, "mysite/index.html")		

def home_global(request):
	response = requests.get('https://api.covid19api.com/summary')
	geodata = response.json()
	geodata_global = geodata["Global"]
	obj,created=WorldData.objects.get_or_create(
		worlddata_updated_at = timezone.now(),
		worlddata_today_deaths = geodata_global["NewDeaths"],
		worlddata_today_confirmed = geodata_global["NewConfirmed"],
		worlddata_today_recovered = geodata_global["NewRecovered"],
		worlddata_total_deaths = geodata_global["TotalDeaths"],
		worlddata_total_confirmed = geodata_global["TotalConfirmed"],
		worlddata_total_recovered = geodata_global["TotalRecovered"],
	)
	return render(request, "mysite/index.html")

def home(request):
	response = requests.get('https://api.covid19api.com/summary')
	geodata = response.json()
	geodata = geodata["Countries"]
	for value in geodata:
		obj,created=CountriesData.objects.get_or_create(
			country_name = value["Country"],
			updated_at = value["Date"],
			today_deaths = value["NewDeaths"],
			today_confirmed = value["NewConfirmed"],
			total_deaths = value["TotalDeaths"],
			total_confirmed = value["TotalConfirmed"],
			total_recovered = value["TotalRecovered"],
			)
	return render(request, "mysite/index.html")
	
def list_of_countries(request):
	country_name=CountriesData.objects.values('country_name')
	total= country_name.count()
	context={"country_name":country_name, "total": total,}
	return render(request, "mysite/index.html", context)

def countries(request):
	name=CountriesName.objects.values('name')
	total= name.count()
	context={"name":name, "total": total}
	return render(request, "mysite/index.html", context)

def make_graph(request, pk_country="India"):
	name=CountriesName.objects.filter(name=pk_country)
	get_data = CountriesData.objects.filter(country_name=pk_country).order_by('-updated_at')
	state_data = {i['state'].replace(" ",""):i['confirmed'] for i in StateData.objects.all().order_by('-updated_on').values()}
	try:
		total_confirmed = get_data.values()[0]["total_confirmed"]
		total_recovered = get_data.values()[0]["total_recovered"]
	except:
		total_confirmed = 0
		total_recovered = 0
	finally:
		context={"name_it" : name[0],
		"get_data" : get_data,
		"country" : pk_country,
		"total_confirmed" : total_confirmed,
		"total_recovered" : total_recovered,
		"state_data":state_data,
		"direct_links":direct_links,
		}
	return render(request, "mysite/create_graph.html", context)


def model_form_upload(request, pk_country):
	country_name=get_object_or_404(CountriesName, name=pk_country)
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES, instance=country_name)
		if form.is_valid():
			form.save()
			messages.success(request, 'Form submission successful !!!')
			return redirect('index')
	else:
		form = DocumentForm(instance=country_name)
	return render(request, 'mysite/model_form_upload.html', {'form': form })

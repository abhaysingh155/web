from django.db import models
from mysite import settings

class CountriesName(models.Model):
	name = models.CharField(max_length=200)
	country_pic = models.CharField(max_length=200)
	alpha3Code = models.CharField(max_length=200, null=True)
	#country_pic = models.ImageField(upload_to='images/', default="images/india.jpg", null=True, blank=True)

	def __str__(self):
		return self.name

class CountriesData(models.Model):
	country_name =  models.CharField(max_length=200)
	updated_at = models.DateTimeField() 
	today_deaths = models.IntegerField( null=True)
	today_confirmed = models.IntegerField( null=True)
	total_deaths = models.IntegerField( null=True)
	total_confirmed = models.IntegerField( null=True) 
	total_recovered = models.IntegerField( null=True) 

	def __str__(self):
		return self.country_name

class WorldData(models.Model):
	worlddata_updated_at = models.DateTimeField() 
	worlddata_today_deaths = models.IntegerField( null=True)
	worlddata_today_confirmed = models.IntegerField( null=True)
	worlddata_today_recovered = models.IntegerField( null=True)
	worlddata_total_deaths = models.IntegerField( null=True)
	worlddata_total_confirmed = models.IntegerField( null=True)
	worlddata_total_recovered = models.IntegerField( null=True) 

	def __str__(self):
		return self.worlddata_updated_at


class StateData(models.Model):
	active = models.IntegerField( null=True)
	confirmed = models.IntegerField( null=True)
	deaths = models.IntegerField( null=True)
	state = models.CharField(max_length=200)
	updated_on = models.DateTimeField(null=True) 

	def __str__(self):
		return self.state


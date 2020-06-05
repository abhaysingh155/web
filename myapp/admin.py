from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CountriesData)
admin.site.register(CountriesName)
admin.site.register(WorldData)
admin.site.register(StateData)

from django.contrib import admin

# Register your models here.
from .models import  Note, Country, AnimalList

admin.site.register(Note)
admin.site.register(Country)
admin.site.register(AnimalList)


from django.contrib import admin
from .models import Benutzer, Fahrerlaubnis, Transportmittel, Fahrt, Reservieren, Bewertung

# Register your models here.
my_models = [Benutzer, Fahrerlaubnis, Transportmittel, Fahrt, Reservieren, Bewertung]
admin.site.register(my_models)

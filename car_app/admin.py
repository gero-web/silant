from django.contrib import admin
from car_app.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
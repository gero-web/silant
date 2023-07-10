from django.contrib import admin
from car_app.models import Car,Service_Company,Client,Model_Steering_Bridge,Model_Drive_Axle,Model_Transmission, \
                           Model_Engine,Model_Technique
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)


class ServiceCompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service_Company, ServiceCompanyAdmin)


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)


class SteeringBridgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model_Steering_Bridge, SteeringBridgeAdmin)

class DriveAxleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model_Drive_Axle, DriveAxleAdmin)


class TransmissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model_Transmission, TransmissionAdmin)


class EngineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model_Engine, EngineAdmin)


class TechniqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Model_Technique, TechniqueAdmin)
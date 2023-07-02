from django.contrib import admin
from django.urls import path
from car_app.views import CarListView, CarCreateView,Service_CompanyCreateView,ClientCreateView,\
                          ModelSteeringBridgeCreateView,ModelDriveAxleCreateView,ModelTransmissionCreateView,\
                          ModelEngineCreateView,ModelTechniqueCraeteView

app_name='car'

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('create_car', CarCreateView.as_view(), name='car_add'),
    path('create_service_company', Service_CompanyCreateView.as_view(), name='service_company'),
    path('create_client', ClientCreateView.as_view(), name='client'),
    path('create_steering_bridge', ModelSteeringBridgeCreateView.as_view(), name='steering_bridge'),
    path('create_drive_axle', ModelDriveAxleCreateView.as_view(), name='drive_axle'),
    path('create_transmission', ModelTransmissionCreateView.as_view(), name='transmission'),
    path('create_engine', ModelEngineCreateView.as_view(), name='engine'),
    path('create_technique', ModelTechniqueCraeteView.as_view(), name='technique'),

]

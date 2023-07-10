from django.contrib import admin
from django.urls import path
from car_app.views import CarListView, CarDetail,CarCreateView,Service_CompanyCreateView,ClientCreateView,\
                          ModelSteeringBridgeCreateView,ModelDriveAxleCreateView,ModelTransmissionCreateView,\
                          ModelEngineCreateView,ModelTechniqueCraeteView,CarUpdateView,Service_CompanyUpdateView,\
                          ClientUpdateView,ModelSteeringBridgeUpdateView,ModelDriveAxleUpdateView,ModelTransmissionUpdateView,\
                          ModelEngineUpdateView,ModelTechniqueCraeteView

app_name='car'

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('car_detail/<int:pk>', CarDetail.as_view(), name='car_detail'),
    path('create_car', CarCreateView.as_view(), name='car_add'),
    path('create_service_company', Service_CompanyCreateView.as_view(), name='service_company'),
    path('create_client', ClientCreateView.as_view(), name='client'),
    path('create_steering_bridge', ModelSteeringBridgeCreateView.as_view(), name='steering_bridge'),
    path('create_drive_axle', ModelDriveAxleCreateView.as_view(), name='drive_axle'),
    path('create_transmission', ModelTransmissionCreateView.as_view(), name='transmission'),
    path('create_engine', ModelEngineCreateView.as_view(), name='engine'),
    path('create_technique', ModelTechniqueCraeteView.as_view(), name='technique'),
    path('update_car/<int:pk>', CarUpdateView.as_view(), name='car_update'),
    path('update_service_company/<int:pk>', Service_CompanyUpdateView.as_view(), name='service_company_update'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('update_steering_bridge/<int:pk>', ModelSteeringBridgeUpdateView.as_view(), name='steering_bridge_update'),
    path('update_drive_axle/<int:pk>', ModelDriveAxleUpdateView.as_view(), name='drive_axle_update'),
    path('update_transmission/<int:pk>', ModelTransmissionUpdateView.as_view(), name='transmission_update'),
    path('update_engine/<int:pk>', ModelEngineUpdateView.as_view(), name='engine_update'),
    path('update_technique/<int:pk>', ModelTechniqueCraeteView.as_view(), name='technique_update'),
]

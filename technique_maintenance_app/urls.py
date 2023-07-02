from django.contrib import admin
from django.urls import path
from technique_maintenance_app.views import TOListView,TOCreateView, KindToCreateView,\
                                                   OrganizationCarriedOutCreateView

app_name='technique_maintenance'

urlpatterns = [
    path('', TOListView.as_view(), name='to_list'),
    path('to_create', TOCreateView.as_view(), name='to_create'),
    path('to_create_kind', KindToCreateView.as_view(), name='to_create_knid'),
    path('to_create_carried', OrganizationCarriedOutCreateView.as_view(), name='to_create_carried_out'),


]

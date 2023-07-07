from django.contrib import admin
from django.urls import path
from technique_maintenance_app.views import TOListView,TOCreateView, TODetail ,KindToCreateView,\
                                                   OrganizationCarriedOutCreateView,KindToUpdateView,TOUpdateView,OrganizationCarriedOutUpdateView

app_name='technique_maintenance'

urlpatterns = [
    path('', TOListView.as_view(), name='to_list'),
    path('to_create', TOCreateView.as_view(), name='to_create'),
    path('to_create_kind', KindToCreateView.as_view(), name='to_create_knid'),
    path('to_create_carried', OrganizationCarriedOutCreateView.as_view(), name='to_create_carried_out'),
    path('to-detail\<int:pk>', TODetail.as_view(), name='to-detail'),
    path('to_update_kind\<int:pk>', KindToUpdateView.as_view(), name='to_update_knid'),
    path('to_update_carried\<int:pk>', OrganizationCarriedOutUpdateView.as_view(), name='to_upate_carried_out'),
    path('to-update\<int:pk>', TOUpdateView.as_view(), name='to-update'),
 
]

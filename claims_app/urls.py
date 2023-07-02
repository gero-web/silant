from django.contrib import admin
from django.urls import path
from claims_app.views import RecoveryCreateView,FailureCreateView, ClaimsListView, ClaimsCreateView
app_name='claims'

urlpatterns = [
    path('', ClaimsListView.as_view(), name='claims_list'),
    path('claims_create', ClaimsCreateView.as_view(), name='claims_create'),
    path('recovery_cteate', RecoveryCreateView.as_view(), name='claims_create_recovery'),
    path('create_failure', FailureCreateView.as_view(), name='claims_create_failure'),
]
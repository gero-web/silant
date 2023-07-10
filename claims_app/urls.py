from django.contrib import admin
from django.urls import path
from claims_app.views import RecoveryCreateView,FailureCreateView, ClaimsDetailView ,ClaimsListView, ClaimsCreateView, \
    ClaimsUpdateView,FailureUpdateView,RecoveryUpdateView


app_name='claims'
urlpatterns = [
    path('', ClaimsListView.as_view(), name='claims_list'),
    path('claims-detail/<int:pk>', ClaimsDetailView.as_view(), name='claims-detail'),
    path('claims_create', ClaimsCreateView.as_view(), name='claims_create'),
    path('recovery_cteate', RecoveryCreateView.as_view(), name='claims_create_recovery'),
    path('create_failure', FailureCreateView.as_view(), name='claims_create_failure'),
    path('claims_update/<int:pk>', ClaimsUpdateView.as_view(), name='claims_update'),
    path('recovery_update/<int:pk>', FailureUpdateView.as_view(), name='claims_update_failure'),
    path('update_failure/<int:pk>', RecoveryUpdateView.as_view(), name='claims_update_recovery'),
]


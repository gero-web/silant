from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from claims_app.models import Claims, Recovery_Method, Failure_Node
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class ClaimsListView(LoginRequiredMixin,ListView):
    model =  Claims
    queryset = Claims.objects.all().select_related('recovery_method', 'failure_node')
    template_name = 'claims\claims_list.html'
    paginate_by = 10

class ClaimsCreateView(LoginRequiredMixin,CreateView):
    template_name = 'claims\claims_create.html'
    fields = '__all__'
    model = Claims
   # permission_required = 'Can add car'

class RecoveryCreateView(LoginRequiredMixin,CreateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Recovery_Method
   # permission_required = 'Can add car'

class FailureCreateView(LoginRequiredMixin,CreateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Failure_Node
   # permission_required = 'Can add car'
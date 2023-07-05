from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from technique_maintenance_app.models import Technique_Maintenance,Kind_Technique_Maintenance,\
                                                    Organization_Tat_Carried_Out
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

class TOListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model =  Technique_Maintenance
    queryset = Technique_Maintenance.objects.all().select_related('service_company','car',\
                                                          'organization_that_carried_TO','kind_technique_maintenance')
    template_name = 'technique_maintenance\TOList.html'

class TODetail(LoginRequiredMixin, DetailView):
    model = Technique_Maintenance
    template_name = 'technique_maintenance\TO-detail.html'

class TOCreateView(LoginRequiredMixin, CreateView):
    model = Technique_Maintenance
    template_name = 'technique_maintenance\TO_create.html'
    fields = '__all__'

class KindToCreateView(LoginRequiredMixin, CreateView):
    model = Kind_Technique_Maintenance
    fields = '__all__'
    template_name = 'root\create_dictionaryi.html'


class OrganizationCarriedOutCreateView(LoginRequiredMixin, CreateView):
    model = Organization_Tat_Carried_Out
    fields = '__all__'
    template_name = 'root\create_dictionaryi.html'

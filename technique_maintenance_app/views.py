from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from technique_maintenance_app.models import Technique_Maintenance,Kind_Technique_Maintenance,\
                                                    Organization_Tat_Carried_Out
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from silant.utils.getFilters import get_filters
from technique_maintenance_app.forms.form_filter import FromFilter
from django.db.models import Q
from silant.utils.check_group import CheckPremGroupMexin


class TOListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model =  Technique_Maintenance
    template_name = 'technique_maintenance\TOList.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = FromFilter()
        context['formFilter'] = form
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        form = FromFilter(self.request.GET)
        is_valid = form.is_valid()
        q = Q()
        if is_valid:
            filters = form.cleaned_data
            q = get_filters(filters) 
        qu = Q()
        if not user.groups.filter(name='manager').exists():
            qu |= Q(('car__client__name__contains', user.username))
            qu |= Q(('service_company__name__contains', user.username)) 
        q &= qu
        self.queryset = Technique_Maintenance.objects.select_related('service_company','car',\
                                                          'organization_that_carried_TO','kind_technique_maintenance').\
                            filter(q)
        return super().get_queryset()


class TODetail(LoginRequiredMixin, DetailView):
    model = Technique_Maintenance
    template_name = 'technique_maintenance\TO-detail.html'

class TOCreateView(LoginRequiredMixin, CheckPremGroupMexin ,CreateView):
    model = Technique_Maintenance
    template_name = 'technique_maintenance\TO_create.html'
    group = ['client', 'service_organization', 'manager', ]
    fields = '__all__'

class KindToCreateView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    model = Kind_Technique_Maintenance
    fields = '__all__'
    template_name = 'root\create_dictionaryi.html'
    group = ['client', 'service_organization', 'manager', ]

class OrganizationCarriedOutCreateView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    model = Organization_Tat_Carried_Out
    fields = '__all__'
    group = ['client', 'service_organization', 'manager', ]
    template_name = 'root\create_dictionaryi.html'
    
    
    
class TOUpdateView(LoginRequiredMixin, CheckPremGroupMexin ,UpdateView):
    model = Technique_Maintenance
    template_name = 'technique_maintenance\TO_create.html'
    group = [ 'manager', ]
    fields = '__all__'

class KindToUpdateView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    model = Kind_Technique_Maintenance
    fields = '__all__'
    template_name = 'root\create_dictionaryi.html'
    group = ['manager', ]

class OrganizationCarriedOutUpdateView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    model = Organization_Tat_Carried_Out
    fields = '__all__'
    group = ['manager', ]
    template_name = 'root\create_dictionaryi.html'


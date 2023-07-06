from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from claims_app.models import Claims, Recovery_Method, Failure_Node
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from claims_app.forms.form_filter import FromFilter
from silant.utils.getFilters import get_filters
from django.db.models import Q


class ClaimsListView(LoginRequiredMixin,ListView):
    model =  Claims
    template_name = 'claims\claims_list.html'
    paginate_by = 10
    
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
        qu |= Q(('car__client__name__contains', user.username))
        qu |= Q(('service_company__name__contains', user.username)) 
        q &= qu
        self.queryset = Claims.objects.select_related('car', 'service_company','recovery_method', 'failure_node').filter(q)
         
        return super().get_queryset()
    
    
class ClaimsCreateView(LoginRequiredMixin,CreateView):
    template_name = 'claims\claims_create.html'
    fields = '__all__'
    model = Claims
   # permission_required = 'Can add car'

class ClaimsDetailView(LoginRequiredMixin, DetailView):
    model = Claims
    template_name ='claims\claims_detail.html'

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
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView,CreateView, UpdateView
from claims_app.models import Claims, Recovery_Method, Failure_Node
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from claims_app.forms.form_filter import FromFilter
from silant.utils.getFilters import get_filters
from django.db.models import Q
from silant.utils.check_group import CheckPremGroupMexin


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
        if not user.groups.filter(name='manager').exists():
            qu |= Q(('car__client__name__contains', user.username))
            qu |= Q(('service_company__name__contains', user.username)) 
        q &= qu
        self.queryset = Claims.objects.select_related('car', 'service_company','recovery_method', 'failure_node').filter(q)
         
        return super().get_queryset()
    
    

class ClaimsDetailView(LoginRequiredMixin, DetailView):
    model = Claims
    template_name ='claims\claims_detail.html'

    
class ClaimsCreateView(LoginRequiredMixin, CheckPremGroupMexin,CreateView):
    template_name = 'claims\claims_create.html'
    fields = '__all__'
    model = Claims
    group = ['service_organization', 'manager', ]
   # permission_required = 'Can add car'

class RecoveryCreateView(LoginRequiredMixin,CheckPremGroupMexin,CreateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Recovery_Method
    group = ['service_organization', 'manager', ]
   # permission_required = 'Can add car'

class FailureCreateView(LoginRequiredMixin,CheckPremGroupMexin,CreateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Failure_Node
    group = ['service_organization', 'manager', ]
   # permission_required = 'Can add car'
   
class ClaimsUpdateView(LoginRequiredMixin, CheckPremGroupMexin,UpdateView):
    template_name = 'claims\claims_create.html'
    fields = '__all__'
    model = Claims
    group = ['manager', ]
   # permission_required = 'Can add car'

class RecoveryUpdateView(LoginRequiredMixin,CheckPremGroupMexin,UpdateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Recovery_Method
    group = ['manager', ]
   # permission_required = 'Can add car'

class FailureUpdateView(LoginRequiredMixin,CheckPremGroupMexin,UpdateView):
    template_name = 'root\create_dictionaryi.html'
    fields = '__all__'
    model = Failure_Node
    group = ['manager', ]
   # permission_required = 'Can add car'
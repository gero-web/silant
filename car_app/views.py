from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import  ListView,CreateView,DetailView, UpdateView
from car_app.models import Car,Service_Company,Client,Model_Steering_Bridge,Model_Drive_Axle,Model_Transmission, \
                           Model_Engine,Model_Technique
from silant.utils.getFilters import get_filters
from car_app.forms.form_filter import FromFilter
from django.forms import ModelForm
from django.db.models import Q
from silant.utils.check_group import CheckPremGroupMexin


# Create your views here.
class CarListView( ListView):
    
    paginate_by = 3
    template_name = 'car\carList.html'
    model = Car
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        form:ModelForm = FromFilter()
        context = super().get_context_data(**kwargs)
        context['formFilter'] = form
        return context
    
    def get_queryset(self):
      t = self.request.GET.getlist('q', '')
      form:ModelForm = FromFilter(self.request.GET)
      user = self.request.user
      if user.is_authenticated: 
        q =()
        is_valid = form.is_valid()
        if is_valid:
            filters = form.cleaned_data
            q = get_filters(filters) 
        qu = Q()
        qu |= Q(('client__name__contains', user.username))
        qu |= Q(('service_company__name__contains', user.username))
        q &= qu
        self.queryset =  Car.objects.select_related('client', 'service_company', 'model_steering_bridge', \
                                                      'model_drive_axle', 'model_transmission', 'model_engine', \
                                                      'model_techique', ).filter(q)
      else:       
            self.queryset =   Car.objects.select_related('client', 'service_company', 'model_steering_bridge', \
                                                      'model_drive_axle', 'model_transmission', 'model_engine', \
                                                      'model_techique', ).filter(head_machine_no__in=t)
      
      return  super(CarListView, self).get_queryset()



class CarCreateView(LoginRequiredMixin, CheckPremGroupMexin ,CreateView):
    template_name = 'car\carCreate.html'
    fields = '__all__'
    model = Car
    success_url = '/'
    group = ['manager']
   # permission_required = 'Can add car'

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'
    template_name ='car\car_detail.html'
    group = ['manager']


class CarUpdateView(LoginRequiredMixin, CheckPremGroupMexin , UpdateView):
    template_name = 'car\carCreate.html'
    fields = '__all__'
    model = Car
    success_url = '/'
    group = ['manager']

class Service_CompanyCreateView(LoginRequiredMixin, CheckPremGroupMexin ,CreateView):
    fields = '__all__'
    model = Service_Company
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ClientCreateView(LoginRequiredMixin,CheckPremGroupMexin ,CreateView):
    fields = '__all__'
    model = Client
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelSteeringBridgeCreateView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    fields = '__all__'
    model = Model_Steering_Bridge
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelDriveAxleCreateView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    fields = '__all__'
    model = Model_Drive_Axle
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelTransmissionCreateView(LoginRequiredMixin, CheckPremGroupMexin ,CreateView):
    fields = '__all__'
    model = Model_Transmission
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelEngineCreateView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    fields = '__all__'
    model = Model_Engine
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelTechniqueCraeteView(LoginRequiredMixin,CheckPremGroupMexin, CreateView):
    fields = '__all__'
    model = Model_Technique
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']
    
    

class Service_CompanyUpdateView(LoginRequiredMixin, CheckPremGroupMexin ,UpdateView):
    fields = '__all__'
    model = Service_Company
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ClientUpdateView(LoginRequiredMixin,CheckPremGroupMexin ,UpdateView):
    fields = '__all__'
    model = Client
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelSteeringBridgeUpdateView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    fields = '__all__'
    model = Model_Steering_Bridge
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelDriveAxleUpdateView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    fields = '__all__'
    model = Model_Drive_Axle
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelTransmissionUpdateView(LoginRequiredMixin, CheckPremGroupMexin ,UpdateView):
    fields = '__all__'
    model = Model_Transmission
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelEngineUpdateView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    fields = '__all__'
    model = Model_Engine
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']

class ModelTechniqueCraeteView(LoginRequiredMixin,CheckPremGroupMexin, UpdateView):
    fields = '__all__'
    model = Model_Technique
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'
    group = ['manager']


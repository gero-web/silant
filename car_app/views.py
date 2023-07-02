from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import  ListView,CreateView,DetailView
from car_app.models import Car,Service_Company,Client,Model_Steering_Bridge,Model_Drive_Axle,Model_Transmission, \
                           Model_Engine,Model_Technique
from django.db.models import Q

# Create your views here.
class CarListView(ListView):
    paginate_by = 50
    template_name = 'car\carList.html'
    model = Car

    def get_queryset(self):
      t = self.request.GET.getlist('q', '')

      print( Service_Company.objects.filter(Q(name__in=t)))
      if not self.request.user.is_authenticated:
            self.queryset =  Car.objects.all().select_related('model_steering_bridge','model_drive_axle',\
                                                'model_transmission','model_engine', 'model_techique' ).\
                                    values('head_machine_no', \
                                            'model_techique', 'model_engine', 'head_engine_no',
                                            'model_transmission',  'head_transmission_no',\
                                            'model_drive_axle', 'head_drive_axle_no',\
                                            'model_steering_bridge', 'head_steering_bridge_no' )
      else:
          self.queryset = Car.objects.all().select_related('client', 'service_company', 'model_steering_bridge', \
                                                      'model_drive_axle', 'model_transmission', 'model_engine', \
                                                      'model_techique', )
      return  super(CarListView, self).get_queryset()



class CarCreateView(LoginRequiredMixin,CreateView):
    template_name = 'car\carCreate.html'
    fields = '__all__'
    model = Car
    success_url = '/'
   # permission_required = 'Can add car'

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'
    template_name ='car\car-detail.html'


class Service_CompanyCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Service_Company
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ClientCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Client
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ModelSteeringBridgeCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Model_Steering_Bridge
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ModelDriveAxleCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Model_Drive_Axle
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ModelTransmissionCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Model_Transmission
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ModelEngineCreateView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Model_Engine
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'

class ModelTechniqueCraeteView(LoginRequiredMixin,CreateView):
    fields = '__all__'
    model = Model_Technique
    template_name = 'root\create_dictionaryi.html'
    success_url = 'create_car'


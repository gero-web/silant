from django.forms import ModelForm
from technique_maintenance_app.models import Technique_Maintenance


class FromFilter(ModelForm):
    
    class Meta:
        model = Technique_Maintenance
        fields = [ 'kind_technique_maintenance', 'car', 'service_company',
                
        ]
        labels = {
            'kind_technique_maintenance': 'Вид ТО',
            'car': 'Зав. номер машины',
            'service_company': 'Сервисная компания',
            
        }
        
    def __init__(self, *args, **kwargs):
        super(FromFilter, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False 
        
         

                
            
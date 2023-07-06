from django.forms import ModelForm
from claims_app.models import Claims


class FromFilter(ModelForm):
    
    class Meta:
        model = Claims
        fields = [ 'failure_node', 'recovery_method', 'service_company',
                
        ]
        labels = {
            'failure_node': 'Узел отказа',
            'recovery_method': 'Способ восстановления',
            'service_company': 'Сервисная компания',
            
        }
        
    def __init__(self, *args, **kwargs):
        super(FromFilter, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False 
        
         

                
            
from django.forms import ModelForm
from car_app.models import Car


class FromFilter(ModelForm):
    
    class Meta:
        model = Car
        fields = [ 'model_techique', 'model_engine', 'model_drive_axle',
                'model_transmission', 'model_steering_bridge',
        ]
        labels = {
            'model_techique': 'Модель техники',
            'model_engine': 'Модель двигателя',
            'model_transmission': 'Модель трансмиссии',
            'model_drive_axle':'Модель ведущего моста',
            'model_steering_bridge': 'Модель ведущего моста',
        }
        
    def __init__(self, *args, **kwargs):
        super(FromFilter, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False 
        
         

                
            
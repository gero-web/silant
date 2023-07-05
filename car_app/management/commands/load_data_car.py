from django.core.management.base import BaseCommand, CommandError
from car_app.models import Car,Client,Model_Drive_Axle,Model_Engine,Model_Steering_Bridge,\
    Model_Technique,Model_Transmission,Service_Company
from django.db.models import Model
from django.conf import settings
import os
import pandas
 
 
 
class Command(BaseCommand):

    
    def create_table(self, table:Model, df:pandas.DataFrame):
        lst = []
        s_dub = set()
        for item in df:
            if item not in s_dub:
                lst.append(table(name=item, description=''))
                s_dub.add(item)
        table.objects.bulk_create(lst) 
    
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'data.xlsx' )
        
        df = pandas.read_excel(io=path,
                    engine='openpyxl',
                    header=2,
                    sheet_name=['машины', ])
        
        df =  df['машины']
        self.create_table( Client, df['Покупатель'])
        self.create_table( Service_Company, df['Сервисная компания'])
        self.create_table( Model_Engine, df['Модель\nдвигателя'])
        self.create_table( Model_Steering_Bridge, df['Модель управляемого моста'])
        self.create_table( Model_Drive_Axle, df['Модель\nведущего моста'])
        self.create_table( Model_Technique, df['Модель \nтехники'])
        self.create_table( Model_Transmission, df['Модель трансмиссии\n(производитель, артикул)'])
          
        
        lst = []
        for row in df.values:
            r = row[1:]
            lst.append(
                Car(
                   model_techique=Model_Technique.objects.get(name=r[0], description=''),
                   head_machine_no=r[1],
                   model_engine=Model_Engine.objects.get(name=r[2], description=''),
                   head_engine_no=r[3],
                   model_transmission=Model_Transmission.objects.get(name=r[4], description=''),
                   head_transmission_no=r[5],
                   model_drive_axle=Model_Drive_Axle.objects.get(name=r[6], description=''),
                   head_drive_axle_no=r[7],
                   model_steering_bridge=Model_Steering_Bridge.objects.get(name=r[8], description=''),
                   head_steering_bridge_no=r[9],
                   date_shipment=r[10],
                   client = Client.objects.get(name=r[11], description=''),
                   сonsignee = r[12],
                   delivery_address = r[13],
                   equipment = r[14],
                   service_company=Service_Company.objects.get(name=r[15], description=''),
                   deliver_contract_no='None',
                    
                )  
            )
            Car.objects.bulk_create(lst, ignore_conflicts=True)

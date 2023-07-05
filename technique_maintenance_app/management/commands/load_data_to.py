from django.core.management.base import BaseCommand, CommandError
from technique_maintenance_app.models import  Car,  Service_Company,Kind_Technique_Maintenance, Technique_Maintenance,\
    Organization_Tat_Carried_Out
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
                    header=0,
                    sheet_name=['ТО output', ])
        
        df =  df['ТО output']
         
        self.create_table( Organization_Tat_Carried_Out, df['Организация, проводившая ТО'])
        self.create_table( Kind_Technique_Maintenance, df['Вид ТО'])
         
        lst = []
        for row in df.values:
             lst.append(
                Technique_Maintenance(
                   kind_technique_maintenance=Kind_Technique_Maintenance.objects.get(name=row[1]),
                   date_holding_TO=row[2],
                   operating_time_mh= row[3],
                   dress_order_no=row[4],
                   dress_order=row[5],
                   organization_that_carried_TO=Organization_Tat_Carried_Out.objects.get(name=row[6]),
                   car = Car.objects.get(head_machine_no=row[0]),
                   service_company = Service_Company.objects.get(pk=1)
                    
                )  
            )
        Technique_Maintenance.objects.bulk_create(lst)
       
       

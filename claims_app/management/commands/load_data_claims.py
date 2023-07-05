from django.core.management.base import BaseCommand, CommandError
from claims_app.models import  Car, Claims, Recovery_Method, Failure_Node, Service_Company
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
                    header=1,
                    sheet_name=['рекламация output', ])
        
        df =  df['рекламация output']
         
        self.create_table( Recovery_Method, df['Способ восстановления'])
        self.create_table( Failure_Node, df['Узел отказа'])
         
        lst = []
        for row in df.values:
             lst.append(
                Claims(
                   date_rejection=row[1],
                   operating_time_mh=row[2],
                   failure_node= Failure_Node.objects.get(name=row[3]),
                   failure_description=row[4],
                   recovery_method=Recovery_Method.objects.get(name=row[5]),
                   used_spare_parts=row[6],
                   date_recovery=row[7],
                   car = Car.objects.get(head_machine_no=row[0]),
                   service_company = Service_Company.objects.get(pk=1),
                   downtime=row[8]
                    
                )  
            )
        Claims.objects.bulk_create(lst, ignore_conflicts=True)
       

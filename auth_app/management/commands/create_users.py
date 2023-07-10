from typing import Any, Optional
from django.core.management import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User,Group
import os
import pandas


class Command(BaseCommand):
    
    def create_user(self, table:User,group ,df:pandas.DataFrame):
        s_dub = set()
        for item in df:
            if item not in s_dub:
                s_dub.add(item)
                item = item[item.index(' ') + 1:].replace('"', '')
                user = table.objects.create_user(username=item,password='123456',)
                user.groups.add(group)
         
        
    def handle(self, *args: Any, **options: Any) -> str | None:
        path = os.path.join(settings.BASE_DIR, 'data.xlsx' )
        
        df = pandas.read_excel(io=path,
                    engine='openpyxl',
                    header=2,
                    sheet_name=['машины', ])
        df =  df['машины']
        
        client_group = Group.objects.get(name='client')
        service_group = Group.objects.get(name='service_organization')
        self.create_user(User, client_group, df['Покупатель'])
        self.create_user(User, service_group, df['Сервисная компания'])
        
        manager =  User.objects.create_superuser("manager", password='123456')
        manager_group = Group.objects.get(name='manager')
        manager.groups.add(manager_group)
         
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

GROUPS = ['client', 'service_organization', 'manager', ]
PERMISSIONS = ['view', 'add', 'delete', 'change']
roles_in_group = {
    'client': {
        'car': ['view', ],
        'claims': ['view',],
        'technique_ maintenance': ['view', 'add','delete', 'change'],
    },
    'service_organization': {
        'car': ['view', ],
        'claims': ['view', 'add','delete', 'change'],
        'technique_ maintenance': ['view', 'add', 'delete', 'change'],
    },
    'manager': {
        'car': ['view', 'add','delete', 'change'],
        'claims': ['view', 'add','delete', 'change'],
        'technique_ maintenance': ['view', 'add','delete', 'change'],
    },
}
class Command(BaseCommand):

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            group_and_role = roles_in_group[group]
            for model, values in group_and_role.items():
                for prem in values:
                    name = 'Can {} {}'.format(prem, model)
                    model_and_prem = Permission.objects.get(name=name)
                    new_group.permissions.add(model_and_prem)




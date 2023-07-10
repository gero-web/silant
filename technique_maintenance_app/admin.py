from django.contrib import admin
from technique_maintenance_app.models import Technique_Maintenance,Kind_Technique_Maintenance,\
                                                    Organization_Tat_Carried_Out
# Register your models here.

class TechniqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Technique_Maintenance, TechniqueAdmin)

class KindAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kind_Technique_Maintenance, KindAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization_Tat_Carried_Out, OrganizationAdmin)
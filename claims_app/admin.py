from django.contrib import admin
from claims_app.models import Claims, Recovery_Method, Failure_Node

# Register your models here.
class ClaimsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Claims, ClaimsAdmin)


class RecoveryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recovery_Method, RecoveryAdmin)


class FailureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Failure_Node, FailureAdmin)
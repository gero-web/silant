from django.core.exceptions import PermissionDenied


class CheckPremGroupMexin:
    group = []
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.groups.filter(name__in = self.group).exists():
           
           return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied(' У вас нет прав для выполнения данного запроса',)
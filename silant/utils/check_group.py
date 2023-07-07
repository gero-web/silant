from django.core.exceptions import PermissionDenied


class CheckPremGroupMexin:
    group = []
    def dispatch(self, request, *args, **kwargs):
        print('trfdsfrdsajmfkds')
        if request.user.groups.filter(name__in = self.group):
           
           return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied(' У вас нет прав для выполнения данного запроса',)
from abc import ABC, abstractmethod
from django.contrib.auth.models import Permission


class UserPermissions(ABC):
    @abstractmethod
    def get_permissions():
        pass


class AdminPermissions(UserPermissions):
    def get_permissions():
        return Permission.objects.all().values_list("id", flat=True)


abc = AdminPermissions()

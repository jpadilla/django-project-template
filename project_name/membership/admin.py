from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin, GroupAdmin as AuthGroupAdmin
from django.contrib.auth.models import Group as AuthGroup

from .models import User, Group


class UserAdmin(AuthUserAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.unregister(AuthGroup)
admin.site.register(Group, AuthGroupAdmin)

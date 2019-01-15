from django.contrib.auth.models import AbstractUser, Group as AuthGroup
from django.utils.translation import ugettext_lazy as _


class Group(AuthGroup):
    class Meta:
        proxy = True
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class User(AbstractUser):
    pass

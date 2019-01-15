from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MembershipConfig(AppConfig):
    name = '{{project_name}}.membership'
    verbose_name = _('membership')

from django.urls import re_path

from talana.apps.core.views import SetUserPassword

app_name = 'core'

urlpatterns = [
    re_path(
        r'^verify-email/'
        '(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})+/$',
        SetUserPassword.as_view(),
        name='set-user-password'
    ),
]

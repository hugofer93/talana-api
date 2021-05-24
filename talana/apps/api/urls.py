from django.urls import include, path

from talana.apps.api.users import urls as users_urls

app_name = 'api'

urlpatterns = [
    path('users/', include(users_urls, namespace='users')),
]

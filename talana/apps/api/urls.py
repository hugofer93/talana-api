from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from talana.apps.api.users import urls as users_urls

app_name = 'api'

urlpatterns = [
    path('users/', include(users_urls, namespace='users')),
]

docs_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]

urlpatterns += docs_urlpatterns

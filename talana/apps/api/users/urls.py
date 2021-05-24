from django.urls import path

from talana.apps.api.users.views import CreateUser, CarryOutDraw

app_name = 'users'

urlpatterns = [
    path('', CreateUser.as_view(), name='create-user'),
    path('carry-out-draw/', CarryOutDraw.as_view(), name='carry-out-draw'),
]

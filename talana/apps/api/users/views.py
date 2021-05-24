from django.contrib.auth import get_user_model

from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from talana.apps.api.users.serializers import (CarryOutDrawSerializer,
                                               CreateUserSerializer)
from talana.apps.core.tasks import (carry_out_draw,
                                    send_verification_email_to_user)
from talana.apps.utils.request import get_host_with_scheme

UserModel = get_user_model()


class CreateUser(ListCreateAPIView):
    http_method_names = ('post', )
    permission_classes = (AllowAny, )
    serializer_class = CreateUserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def send_mail(self, serializer: Serializer) -> None:
        """Send mail to user in background with Celery.

        Args:
            serializer (Serializer): Serializer instance.
        """
        user_id = serializer.instance.id
        host = get_host_with_scheme(self.request)
        send_verification_email_to_user.delay(user_id, host)

    def perform_create(self, serializer) -> None:
        super().perform_create(serializer)
        self.send_mail(serializer)


class CarryOutDraw(GenericAPIView):
    http_method_names = ('post', )
    serializer_class = CarryOutDrawSerializer

    # should be changed for users with permissions
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.data.get('carry_out_draw'):
            carry_out_draw.delay()
        winner_user = UserModel.objects.get_winning_user()
        if not winner_user:
            data = {'winner_user': 'No winner yet.'}
            return Response(data=data)
        data = {
            'user_id': winner_user.id,
            'username': winner_user.username,
        }
        return Response(data=data)

from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.fields import BooleanField
from django.db.utils import IntegrityError

from rest_framework.serializers import (BooleanField, CharField, EmailField,
                                        IntegerField, Serializer,
                                        ValidationError)

UserModel = get_user_model()


class CreateUserSerializer(Serializer):
    id = IntegerField(read_only=True)
    username = CharField(max_length=40, required=True,
                         validators=[UnicodeUsernameValidator(), ])
    email = EmailField(max_length=100, required=True)
    first_name = CharField(max_length=30, required=True)
    last_name = CharField(max_length=80, required=True)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        try:
            user = UserModel.objects.create_user(**validated_data)
        except IntegrityError:
            error = {'error': ['User already exists.',
                               ValidationError.default_detail, ]}
            raise ValidationError(error)
        return user


class CarryOutDrawSerializer(Serializer):
    carry_out_draw = BooleanField(required=True)


def serialize_carry_out_draw(data: dict) -> dict:
    carry_out_draw = data.get('carry_out_draw', False)
    carry_out_draw = bool(carry_out_draw)
    data = {'carry_out_draw': carry_out_draw}
    return data

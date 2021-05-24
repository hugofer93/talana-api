from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from talana.apps.utils.tokens import email_token_generator

UserModel = get_user_model()


def send_verification_email_user(user_id: int, host: str) -> bool:
    """Send the verification email to the user.

    Args:
        user_id (int): User id.
        host (str): Server name in http request.

    Returns:
        bool: If the email is sent.
    """
    try:
        user = UserModel.objects.get_user(user_id)
    except UserModel.DoesNotExist:
        return False

    SUBJECT = 'Verify your email | TALANA'
    kwargs = {
        'token': email_token_generator.make_token(user),
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk))
    }

    url = reverse('core:set-user-password', kwargs=kwargs)
    context = {
        'subject': SUBJECT,
        'username': user.username,
        'host': host,
        'url': url,
    }
    raw_message = render_to_string('utils/verification-email.txt',
                                   context=context)
    html_message = render_to_string('utils/verification-email.html',
                                    context=context)
    sent = send_mail(SUBJECT, raw_message, settings.EMAIL_HOST_USER,
                     [user.email, ], html_message=html_message)
    sent = bool(sent)
    return sent

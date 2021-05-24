from django.contrib.auth import get_user_model

from talana import celery_app
from talana.apps.utils.mail import send_verification_email_user

UserModel = get_user_model()


@celery_app.task
def send_verification_email_to_user(user_id: int, host: str) -> bool:
    """Send verification mail to the user in the background.

    Args:
        user (int): User id.
        host (str): Server name in http request.

    Returns:
        bool: If it's successful.
    """
    sent = send_verification_email_user(user_id, host)
    sent = bool(sent)
    return sent


@celery_app.task
def carry_out_draw() -> bool:
    """Get a random verified user.

    Returns:
        bool: If winner user exists.
    """
    winner_user = UserModel.objects.get_random_verified_user()
    if not winner_user.pk:
        return False
    return True

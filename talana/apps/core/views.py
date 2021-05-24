from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from talana.apps.utils.tokens import email_token_generator

UserModel = get_user_model()


class SetUserPassword(TemplateView):
    """Concrete view to confirm the User."""
    form_class = SetPasswordForm
    http_method_names = ('get', 'post')
    template_name = 'core/set-user-password.html'

    def get_valid_user(self, uidb64):
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get_user(user_id)
        except UserModel.DoesNotExist:
            user = None
        return user

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        user = self.get_valid_user(uidb64)

        if (user and not user.is_verified
                and email_token_generator.check_token(user, token)):
            return super().get(request, *args, **kwargs)
        raise PermissionDenied()

    def post(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        user = self.get_valid_user(uidb64)

        if (user and email_token_generator.check_token(user, token)):
            form = self.form_class(user=user, data=request.POST)
            if not form.is_valid():
                return self.render_to_response(
                    self.get_context_data(form=form))

            user = form.save(commit=False)
            user.is_verified = True
            user.save()
            data = {'success': True}
            return JsonResponse(data, safe=False)
        raise PermissionDenied()

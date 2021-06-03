from django.contrib.admin import register as admin_resgiter
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


@admin_resgiter(UserModel)
class UserAdmin(DjangoUserAdmin):
    """Custom User Admin for AdminSite"""
    list_display = ('username', 'email', 'is_verified', 'is_winner',
                    'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_verified', 'is_winner')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_verified', 'is_winner', 'is_staff',
                       'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

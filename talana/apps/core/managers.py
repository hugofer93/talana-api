from typing import Optional

from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db.models import Model, QuerySet

from talana.apps.utils.random import get_random_value_in_list


class UserManager(DjangoUserManager):
    """Custom manager for User Model."""

    def all_active_users(self) -> QuerySet:
        """Active users list.

        Returns:
            QuerySet: User list.
        """
        all_users = self.all().filter(is_active=True)
        return all_users

    def get_user(self, user_id: int) -> Model:
        """Get an active user.

        Args:
            user_id (int): User id.

        Returns:
            UserModel: User instance.
        """
        user = self.all_active_users().get(id=user_id)
        return user

    def get_winning_user(self) -> Optional[Model]:
        """Get and check the winning user.

        Returns:
            Optional[Model]: User instance, else QuerySet.none().
        """
        winning_user = self.all().filter(is_winner=True)

        # if there is more than one winner,
        # the 'is_winner' field is updated.
        # none is returned.
        if winning_user.count() > 1:
            winning_user.update(is_winner=False)
            winning_user = self.none()

        # if there is no winner, none is returned.
        elif winning_user.count() == 0:
            winning_user = self.none()
        return winning_user.first()

    def get_verified_users(self) -> QuerySet:
        """Get verified and active users.

        Returns:
            QuerySet: Verified users.
        """
        verified_users = self.all_active_users().filter(is_verified=True)
        return verified_users

    def get_random_verified_user(self) -> Model:
        """Get a random verified user.

        Returns:
            UserModel: User instance.
        """
        winner_user = self.get_winning_user()
        if winner_user:
            return winner_user
        verified_users = self.get_verified_users()
        verified_users_id = verified_users.values_list('id', flat=True)
        winning_user_id = get_random_value_in_list(list(verified_users_id))
        winner_user = verified_users.get(id=winning_user_id)
        winner_user.is_winner = True
        winner_user.save()
        return winner_user

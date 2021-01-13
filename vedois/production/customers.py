from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from vedois.production.models import UserTerminal


class CustomerBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        if not username or not password:
            return None

        #User = get_user_model()

        try:
            user = UserTerminal.objects.get(username=username)

        except UserTerminal.DoesNotExist:
            UserTerminal().set_password(password)

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        return None

    def get_user(self, user_id):

        try:
            return UserTerminal.objects.get(pk=user_id)
        except Exception as ex:
            print(str(ex))
            return None
from rest_framework import viewsets
from django.shortcuts import render
from django.core.exceptions import ValidationError

from vedois.production import models
from vedois.production import serializers


# Create your views here.
class UserTerminalViewSet(viewsets.ModelViewSet):
    queryset = models.UserTerminal.objects.all()
    serializer_class = serializers.UserTerminalSerializer

    @staticmethod
    def login(request):

        if not request.POST:
            return None

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)

        if not username and not password:
            raise ValidationError('User or password not informed')

        # Validates that the user exists
        User = models.UserTerminal.objects.get(username=username)
        if not User.username == username:
            raise ValidationError('User does not exist')

        # Validates the user password
        # if not User.password == make_password(password):
        if not User.check_password(password):
            raise ValidationError('Invalid password')

        # Registering the user in the session
        if not request.session.get('user_id') == User.username:
            request.session['user_id'] = User.username

    @staticmethod
    def logout(request):

        try:
            del request.session['user_id']
        except KeyError:
            pass


def do_login(request):
    return render(request, 'login.html')


def do_logout(request):
    return render(request, 'logout.html')
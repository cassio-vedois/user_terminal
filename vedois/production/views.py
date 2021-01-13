from rest_framework import viewsets
from vedois.production import models
from vedois.production import serializers


# Create your views here.
class UserTerminalViewSet(viewsets.ModelViewSet):
    queryset = models.UserTerminal.objects.all()
    serializer_class = serializers.UserTerminalSerializer


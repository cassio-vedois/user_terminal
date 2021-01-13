from rest_framework import serializers
from vedois.production import models


class UserTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserTerminal
        fields = '__all__'


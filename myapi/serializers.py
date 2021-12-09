from rest_framework import serializers
from .models import Benutzer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benutzer
        fields = '__all__'

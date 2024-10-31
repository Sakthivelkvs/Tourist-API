from .models import *
from rest_framework import  serializers

class TouristSerializer(serializers.ModelSerializer):
    Image=serializers.ImageField(required=False)

    class Meta:
        model = TouristApp
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegister
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

from rest_framework import serializers 
from .models import Programador

class programadorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Programador 
        fields = '__all__'
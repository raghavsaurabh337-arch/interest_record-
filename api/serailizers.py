from rest_framework import serializers
from .models import Home

class homeSerializaers(serializers.ModelSerializer):
     class Meta:
          model=Home
          field= '__all__'

from rest_framework import serializers
from project.models import kelvin,Tag
from users.models import profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjetcSerializer(serializers.ModelSerializer):
    Tags=TagSerializer(many=True)
    class Meta:
        model = kelvin
        fields = '__all__'


from .models import Number
from rest_framework import serializers


class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()

    def create(self, validated_data):
        return Number.objects.create(**validated_data)

    class Meta:
        model = Number
        fields = '__all__'

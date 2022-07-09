from rest_framework import serializers
from .models import Roll


class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = ['value', 'result']
    # value = serializers.IntegerField(read_only=True)
    # result = serializers.CharField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Roll.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.value = validated_data.get('value', instance.value)
    #     instance.result = validated_data.get('result', instance.result)
    #     return instance

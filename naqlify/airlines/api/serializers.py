from rest_framework import serializers
from faker import Faker

fake = Faker()


class AirlinesSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    logo = serializers.URLField()
    slogan = serializers.CharField(max_length=100)
    head_quaters = serializers.CharField(max_length=100)
    website = serializers.URLField()
    established = serializers.IntegerField()

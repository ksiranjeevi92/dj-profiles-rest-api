from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serailize a name field testing our API View"""
    name = serializers.CharField(max_length=10)
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testinng our APIView."""
    name = serializers.Charfield(max_length=10)

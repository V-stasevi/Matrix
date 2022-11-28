from rest_framework import serializers

class MatSerializer(serializers.Serializer):
    cols = serializers.IntegerField()
    rows = serializers.IntegerField()
    args = serializers.CharField()
    transposed = serializers.CharField()
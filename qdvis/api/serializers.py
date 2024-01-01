from rest_framework import serializers


class XyGraphSerializer(serializers.Serializer):
    x_value = serializers.FloatField()
    y_value = serializers.FloatField()


class CheckGpuSerializer(serializers.Serializer):
    utilz_gpu = serializers.IntegerField()
    hms_time = serializers.CharField()

from rest_framework import serializers

from measurement.models import Sensor, Measurement

class SensorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'created_at', 'temperature', 'sensor']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerialiser(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

class SensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

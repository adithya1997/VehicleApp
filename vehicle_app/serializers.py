from rest_framework import serializers
from vehicle_app.models import VehicleOrder

class VehicleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOrder
        fields = ('__all__')

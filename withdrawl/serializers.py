from rest_framework import serializers
from .models import Requests

class RequestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['id', 'PlayerID', 'PaymentMethod', 'Amount', 'Time']
from cinema.models import Cinema
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'city', 'address', 'postal_code', 'phone_number')
        read_only_fields = fields

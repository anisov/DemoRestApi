from rest_framework import serializers
from cars.models import Car
from common.serializers import UserSerializer


class CarsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Car
        fields = ('id', 'vin', 'car_type', 'user')


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'

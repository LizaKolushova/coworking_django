from rest_framework import serializers
from .models import Place, Booking, Payment, Rate, AuthUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

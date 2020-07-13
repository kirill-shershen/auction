from rest_framework import serializers
from app.models import Animal, Lot, Bid, User

class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = ['id', 'owner', 'animaltype', 'breed', 'name']

class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = ['id', 'animal', 'price']

class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ['id', 'lot', 'value', 'author']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'balance']


class BidAcceptSerializer(serializers.Serializer):
    accept = serializers.BooleanField(required=True)


from rest_framework import serializers

from thenewboston.constants.network import VERIFY_KEY_LENGTH


class AccountBalanceSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=VERIFY_KEY_LENGTH)
    balance = serializers.DecimalField(max_digits=32, decimal_places=16)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

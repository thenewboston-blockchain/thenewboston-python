from rest_framework import serializers

from thenewboston.constants.network import BALANCE_LOCK_LENGTH, VERIFY_KEY_LENGTH


class NetworkTransactionSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=32, decimal_places=16)
    balance_key = serializers.CharField(max_length=BALANCE_LOCK_LENGTH)
    recipient = serializers.CharField(max_length=VERIFY_KEY_LENGTH)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def validate_amount(amount):
        """
        Check that amount is not 0
        """

        if amount == 0:
            raise serializers.ValidationError('Tx amount can not be 0 (Tx should be excluded)')

        return amount

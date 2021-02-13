from rest_framework import serializers

from thenewboston.constants.network import ACCEPTED_FEE_LIST, MAX_POINT_VALUE, MIN_POINT_VALUE, VERIFY_KEY_LENGTH
from thenewboston.utils.serializers import validate_keys


class NetworkTransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField(max_value=MAX_POINT_VALUE, min_value=MIN_POINT_VALUE)
    fee = serializers.ChoiceField(choices=ACCEPTED_FEE_LIST, required=False)
    recipient = serializers.CharField(max_length=VERIFY_KEY_LENGTH, min_length=VERIFY_KEY_LENGTH)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        """Check that there are no additional keys included in the data"""
        validate_keys(self, data)

        return data

    @staticmethod
    def validate_amount(amount):
        """Check that amount is not 0"""
        if amount == 0:
            raise serializers.ValidationError('Tx amount can not be 0 (Tx should be excluded)')

        return amount

    @staticmethod
    def validate_recipient(recipient):
        """Check that recipient is a valid hexadecimal"""
        try:
            int(recipient, 16)
        except ValueError:
            raise serializers.ValidationError('Recipient must be a valid hexadecimal')

        return recipient

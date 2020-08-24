from rest_framework import serializers

from thenewboston.constants.network import MAX_POINT_VALUE, MIN_POINT_VALUE, VERIFY_KEY_LENGTH


class NetworkTransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField(max_value=MAX_POINT_VALUE, min_value=MIN_POINT_VALUE)
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

    @staticmethod
    def validate_recipient(recipient):
        """
        Check recipient length
        """

        if len(recipient) != VERIFY_KEY_LENGTH:
            raise serializers.ValidationError(f'recipient must be {VERIFY_KEY_LENGTH} characters long')

        return recipient

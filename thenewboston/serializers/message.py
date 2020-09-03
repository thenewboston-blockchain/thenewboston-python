from rest_framework import serializers

from thenewboston.constants.network import BALANCE_LOCK_LENGTH
from thenewboston.serializers.network_transaction import NetworkTransactionSerializer


class MessageSerializer(serializers.Serializer):
    balance_key = serializers.CharField(max_length=BALANCE_LOCK_LENGTH)
    txs = NetworkTransactionSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        """
        Validate Txs exist
        """

        if not data['txs']:
            raise serializers.ValidationError('Invalid Txs')

        return data

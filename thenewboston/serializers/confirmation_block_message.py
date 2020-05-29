from rest_framework import serializers

from thenewboston.serializers.account_balance import AccountBalanceSerializer
from thenewboston.serializers.network_block import NetworkBlockSerializer


class ConfirmationBlockMessageSerializer(serializers.Serializer):
    block = NetworkBlockSerializer()
    updated_balances = AccountBalanceSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

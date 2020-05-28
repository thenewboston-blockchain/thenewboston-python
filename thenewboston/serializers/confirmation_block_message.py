from rest_framework import serializers

from thenewboston.serializers.account_balance import AccountBalanceSerializer
from thenewboston.serializers.block import BlockSerializer


class ConfirmationBlockMessageSerializer(serializers.Serializer):
    block = BlockSerializer()
    updated_balances = AccountBalanceSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

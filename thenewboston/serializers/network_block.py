from rest_framework import serializers

from thenewboston.blocks.signatures import verify_signature
from thenewboston.constants.network import SIGNATURE_LENGTH, VERIFY_KEY_LENGTH
from thenewboston.serializers.message import MessageSerializer
from thenewboston.utils.serializers import validate_keys
from thenewboston.utils.tools import sort_and_encode


class NetworkBlockSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=VERIFY_KEY_LENGTH, min_length=VERIFY_KEY_LENGTH)
    message = MessageSerializer()
    signature = serializers.CharField(max_length=SIGNATURE_LENGTH, min_length=SIGNATURE_LENGTH)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        """
        Validate signature
        Validate Tx recipients are unique
        Validate account_number (the sender) is not included as a Tx recipient
        """

        account_number = data['account_number']
        message = data['message']
        txs = message['txs']
        signature = data['signature']

        verify_signature(
            message=sort_and_encode(message),
            signature=signature,
            verify_key=account_number
        )

        recipient_list = [tx['recipient'] for tx in txs]
        recipient_set = set(recipient_list)

        if len(recipient_list) != len(recipient_set):
            raise serializers.ValidationError('Tx recipients must be unique')

        if account_number in recipient_set:
            raise serializers.ValidationError('Block account_number not allowed as Tx recipient')

        validate_keys(self, data)

        return data

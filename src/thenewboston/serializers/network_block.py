from rest_framework import serializers

from thenewboston.blocks.signatures import verify_signature
from thenewboston.constants.network import BANK, PRIMARY_VALIDATOR, SIGNATURE_LENGTH, VERIFY_KEY_LENGTH
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
        """Validate signature, unique Tx recipients, unique Tx fees and account_number not included as a Tx recipient"""
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

        bank_fee_exists = False
        primary_validator_fee_exists = False

        for tx in txs:
            fee = tx.get('fee', None)

            if fee is None:
                continue

            if fee == BANK:

                if bank_fee_exists:
                    raise serializers.ValidationError('Multiple bank fees not allowed')
                else:
                    bank_fee_exists = True

            if fee == PRIMARY_VALIDATOR:

                if primary_validator_fee_exists:
                    raise serializers.ValidationError('Multiple primary validator fees not allowed')
                else:
                    primary_validator_fee_exists = True

        validate_keys(self, data)

        return data

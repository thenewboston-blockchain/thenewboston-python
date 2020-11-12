from rest_framework import serializers

from thenewboston.constants.network import HEAD_HASH_LENGTH, MAX_POINT_VALUE, MIN_POINT_VALUE, PROTOCOL_CHOICES, \
    VERIFY_KEY_LENGTH

"""
The PrimaryValidatorSerializer is used as a base class to ensure that a nodes primary validator is properly configured
- used during the connection process
"""


class PrimaryValidatorSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=VERIFY_KEY_LENGTH)
    default_transaction_fee = serializers.IntegerField(max_value=MAX_POINT_VALUE, min_value=MIN_POINT_VALUE)
    ip_address = serializers.IPAddressField(protocol='both')
    node_identifier = serializers.CharField(max_length=VERIFY_KEY_LENGTH)
    port = serializers.IntegerField(allow_null=True, max_value=65535, min_value=0, required=False)
    protocol = serializers.ChoiceField(choices=PROTOCOL_CHOICES)
    root_account_file = serializers.URLField()
    root_account_file_hash = serializers.CharField(max_length=HEAD_HASH_LENGTH)
    seed_block_identifier = serializers.CharField(allow_blank=True, max_length=HEAD_HASH_LENGTH)
    version = serializers.CharField(max_length=32)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

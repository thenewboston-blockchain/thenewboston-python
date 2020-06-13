from rest_framework import serializers

from thenewboston.constants.network import SIGNATURE_LENGTH, VERIFY_KEY_LENGTH
from thenewboston.serializers.message import MessageSerializer


class NetworkBlockSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=VERIFY_KEY_LENGTH)
    message = MessageSerializer()
    signature = serializers.CharField(max_length=SIGNATURE_LENGTH)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

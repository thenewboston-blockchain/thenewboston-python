HTTP = 'http'
HTTPS = 'https'

PROTOCOL_CHOICES = [
    (HTTP, HTTP),
    (HTTPS, HTTPS),
]

PROTOCOL_LIST = [HTTP, HTTPS]

ACCEPTED = 'ACCEPTED'
DECLINED = 'DECLINED'
PENDING = 'PENDING'

REGISTRATION_STATUS_CHOICES = [
    (ACCEPTED, ACCEPTED),
    (DECLINED, DECLINED),
    (PENDING, PENDING),
]

BANK = 'BANK'
VALIDATOR = 'VALIDATOR'

BALANCE_LOCK_LENGTH = 64
BLOCK_IDENTIFIER_LENGTH = 64
HEAD_HASH_LENGTH = 64
SIGNATURE_LENGTH = 128
VERIFY_KEY_LENGTH = 64

MIN_POINT_VALUE = 0.0000000000000001

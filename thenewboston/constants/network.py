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
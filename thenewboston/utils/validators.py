import math

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from thenewboston.constants.network import SIGNATURE_LENGTH


def validate_is_real_number(value):
    """
    Validate value is real number, does not allow Infinity, -Infinity, or NaN
    """

    if not value:
        return

    if math.isnan(value):
        raise ValidationError(
            _('NaN is not allowed'),
            params={'value': value},
        )

    if math.isinf(value):
        raise ValidationError(
            _('Infinity is not allowed'),
            params={'value': value},
        )


def validate_is_signature_length(value):
    """
    Validate value is length of signature
    """

    if len(value) != SIGNATURE_LENGTH:
        raise ValidationError(
            _(f'Length of {SIGNATURE_LENGTH} required'),
            params={'value': value},
        )

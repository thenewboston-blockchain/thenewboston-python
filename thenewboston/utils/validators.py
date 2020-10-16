import math

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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

import pytz
from factory import Faker

from ..models.confirmation_service import ConfirmationService
from .created_modified import CreatedModifiedFactory


class ConfirmationServiceFactory(CreatedModifiedFactory):
    end = Faker('date_time', tzinfo=pytz.utc)
    start = Faker('date_time', tzinfo=pytz.utc)

    class Meta:
        model = ConfirmationService

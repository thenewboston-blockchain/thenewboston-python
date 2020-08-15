from factory import Faker
from factory.django import DjangoModelFactory

from ..models.created_modified import CreatedModified


class CreatedModifiedFactory(DjangoModelFactory):
    created_date = Faker('date')
    modified_date = Faker('date')

    class Meta:
        model = CreatedModified
        abstract = True

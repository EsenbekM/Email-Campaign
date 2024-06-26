from django.db import models, transaction

from src.common.exceptions import ObjectNotFoundException, UnkownException


class BaseService:
    model = None

    @classmethod
    def get(cls, select_: list = [], prefetch_: list = [], **filters):
        try:

            return (
                cls.model.objects.select_related(*select_)
                .prefetch_related(*prefetch_)
                .get(**filters)
            )
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException

    @classmethod
    def list(
        cls,
        filters: dict = {},
        exclude: dict = {},
        order: list[str] = [],
        search: list = [],
        select_: list = [], 
        prefetch_: list = []
    ) -> models.QuerySet:
        return (
            cls.model.objects.filter(*search, **filters)
            .exclude(**exclude)
            .order_by(*order)
            .select_related(*select_)
            .prefetch_related(*prefetch_)
        )

    @classmethod
    def create(cls, **data):
        try:
            with transaction.atomic():
                obj = cls.model.objects.create(**data)
                return obj
        except Exception as e:
            raise UnkownException(e)

    @classmethod
    def update(cls, filter_data: dict = {}, **data):
        try:
            with transaction.atomic():
                updated = cls.model.objects.filter(**filter_data).update(**data)
                return updated
        except Exception as e:
            raise UnkownException(e)

    @classmethod
    def delete(cls, **filter):
        try:
            with transaction.atomic():
                cls.model.objects.get(**filter).delete()
                return True
        except cls.model.__class__.DoesNotExist:
            raise ObjectNotFoundException
        except Exception as e:
            raise UnkownException(e)

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    is_active = models.BooleanField(
        default=True, verbose_name=_("is active"), db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created at"), db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        abstract = True

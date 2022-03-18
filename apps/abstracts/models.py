from django.db import models

class AbstractClass(models.Model):

    datatime_created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now=True
    )
    datatime_lifetime = models.DateTimeField(
        verbose_name='время существования',
        auto_now=True
    )
    datatime_deleted = models.DateTimeField(
        verbose_name='время удаления',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
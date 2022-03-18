from datetime import (
    datetime,
)
from django.db import models

from abstracts.models import AbstractClass

from django.contrib.auth.models import User

class Task(AbstractClass):

    datatime_created = models.OneToOneField(
        AbstractClass, on_delete=models.PROTECT
    )
    leadtime = models.DateField(
        'время выполнения'
    )
    user = models.OneToOneField(
        User, on_delete=models.PROTECT
    )
    description = models.TextField(
        'Описание'
    )
    active = models.BooleanField(
        default=True
    )

    class Meta:
       
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
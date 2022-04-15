from datetime import (
    datetime,
)
from django.db import models

from abstracts.models import AbstractClass

from django.contrib.auth.models import User

class Task(AbstractClass):
    TASK_NAME_MAX_LENGTH = 30

    todo = models.CharField(
        max_length = TASK_NAME_MAX_LENGTH
    )

    leadtime = models.DateTimeField(
        verbose_name='время выполнения'
    )
    user = models.OneToOneField(
        User, 
        on_delete=models.PROTECT
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.todo} | {self.user} | {self.active}'

    class Meta:
        ordering =(
            'todo',
        )
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    
from django.contrib import admin

from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User

from . models import (
    Task,
)

class TaskAdmin(admin, ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_lifetime',
        'datetime_deleted',
        )
    list_display = (
        'todo',
        'user',
        'active',
    )
admin.site.register(
    Task, TaskAdmin
)    
# Register your models here.

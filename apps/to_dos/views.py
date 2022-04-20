from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Requset

from django.db.models import QuerySet
from django.contrib.auth.models import User

from to_dos.models import Task
from . serializers import TaskSerializer

class TaskViewSet(ViewSet):

    permissions_classes: tuple = (
        permissions.AllowAny
    )
    queryset: QuerySet = Task.objects.get_not_deleted()
    
    def list(self, request: DRF_Requset) -> DRF_Response:

        serializers: TaskSerializer = \
            TaskSerializer(
                self.queryset,
                many=True
            )
        return DRF_Response(
            {'response': serializers.data}
        )
    
    def retrieve(self, request: DRF_Requset, pk: int = 0) -> DRF_Response:

        custom_task: Optional[Task] = None
        try:
            custom_task = self.queryset().get(
                id=pk
            )
        except Task.DoesNotExist:
            return DRF_Response(
                {'response': 'Не нашел такой домашки'}
            )
        serializer: TaskSerializer = \
            TaskSerializer(
                custom_task
            )

        return DRF_Response(
            {'response': serializer.data}
        )
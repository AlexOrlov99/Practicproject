from typing import Optional
from django.db.models import(
    QuerySet,
    )
from django.views import View
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from to_dos.models import Task

from to_dos.forms import TaskForm

class TodoView(View):

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwags: dict
    ) -> HttpResponse:

        tasks: QuerySet = Task.objects.all()
        template_name: str = 'to_dos/todo.html'

        return render(
            request,
            template_name
        )


class CreatedView(View):
    form: TaskForm = TaskForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwags: dict
    ) -> HttpResponse:

        form: TaskForm = self.form(
            request.POST
        )
        context: dict = {
            'ctx_form': form
        }
        template_name: str = 'to_dos/todo.html'

        return render(
            request,
            template_name,
            context
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
        ) -> HttpResponse:

        _form: TaskForm = self.form(
            request.POST
        )
        if not _form.is_valid():
            context: dict = {
                'ctx_form': _form
            }
            return render(
                request,
                'to_dos/created.html',
                context
            )
        task: Task = _form.save(
            commit=False
        )
        context: dict = {
            'ctx_form': form
        }
        homework.user = request.user
        homework.save()

        return render(
            request,
            'to_dos/created.html',
            context
        )

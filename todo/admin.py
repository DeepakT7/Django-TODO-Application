# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo', 'isCompleted']

admin.site.register(Todo, TodoAdmin)
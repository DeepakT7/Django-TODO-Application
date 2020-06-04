# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):

    todo = models.CharField(max_length = 128, blank = False)
    isCompleted = models.BooleanField(default = False)


    def __str__(self):
        return self.todo
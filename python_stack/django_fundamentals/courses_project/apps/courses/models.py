# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "%s" % (self.name)


class Description(models.Model):
    desc = models.TextField()
    course = models.ForeignKey(Course, related_name="courses")

    def __str__(self):
        return "%s" % (self.desc)
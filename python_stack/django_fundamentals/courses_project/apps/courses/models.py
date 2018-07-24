# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def validator(self, postData):
        errors = []
        name = postData['name']
        desc = postData['desc']

        # Require the course name to be more than 5 characters 
        # and the description to be more than 15 characters.
        if len(name) < 6:
            errors.append('Course Name must be between 6 and 255 characters')
        if len(desc) < 16:
            errors.append('Description must be between 16 and 255 characters')

        if len(errors) > 0:
            return (False, errors)     
        
        try:
            course = self.create(name=name, desc=desc)
            return (True, course)
        except:
            errors.append('An unknown error has occurred. Please try again.')
            return (False, errors)


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "%s" % (self.name)

    objects = CourseManager()
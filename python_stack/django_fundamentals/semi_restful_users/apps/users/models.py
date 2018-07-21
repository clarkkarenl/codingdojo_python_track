# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

# regex to ensure email is in 'foo@bar.com' format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# UserManager handles validation of POST data
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']

        if len(first_name) < 1 or len(first_name) > 254:
            errors.append('First Name must be between one and 255 characters')
        if len(last_name) < 1 or len(last_name) > 254:
            errors.append('Last Name must be between one and 255 characters')
        if len(email) < 1 or not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email address')

        if len(errors) > 0:
            return (False, errors)

        try:
            self.get(email=email)
            errors.append('That is not a valid email')
            return (False, errors)
        except:
            user = self.create(first_name=first_name, last_name=last_name, email=email)
            return (True, user)


# User class definition
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # Connect an instance of UserManager to the User
    # model overwriting the old hidden objects key
    # with a new one with extra properties
    objects = UserManager()

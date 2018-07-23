# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

# regex to ensure email is in 'foo@bar.com' format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# UserManager handles validation of POST data
class UserManager(models.Manager):
    def user_create_validator(self, postData):
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


    def user_update_validator(self, postData):
        errors = []
        usr = User.objects.get(id=postData['id'])
        usr_id = usr.id
        usr.new_first_name = postData['first_name']
        usr.new_last_name = postData['last_name']
        usr.new_email = postData['email']

        if len(usr.new_first_name) < 1 or len(usr.new_first_name) > 254:
            errors.append('First Name must be between one and 255 characters')
        if len(usr.new_last_name) < 1 or len(usr.new_last_name) > 254:
            errors.append('Last Name must be between one and 255 characters')
        if len(usr.new_email) < 1 or not EMAIL_REGEX.match(usr.new_email):
            errors.append('Please enter a valid email address')

        # For updates, we have to allow the same email to be posted as
        # the user might not want to change their email BUT we can't
        # allow a user to change their email to that of another user!
        if usr.email != usr.new_email:
            if User.objects.filter(email=usr.new_email).count() > 0:
                errors.append('That is not a valid email')
        
        if len(errors) > 0:
            return (False, errors)

        try:
            user = self.filter(id=usr_id).update(first_name=usr.new_first_name,last_name=usr.new_last_name, email=usr.new_email)
            return (True, user) 
        except:
            errors.append("The update operation failed for unknown reasons")
            return (False, errors)


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

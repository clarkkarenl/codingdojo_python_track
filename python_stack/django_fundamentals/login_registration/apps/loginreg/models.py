# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_REGEX = re.compile(r'^[a-zA-Z]$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = []
        new_user = user.id
        new_user.first_name = postData['first_name']
        new_user.last_name = postData['last_name']
        new_user.birthdate = postData['birthdate']
        new_user.email = postData['email'] 
        new_user.password = postData['password'] 
        new_user.confirm_pw = postData['confirm_pw']

        # First Name - Required; No fewer than 2 characters; letters only
        if len(new_user.first_name) < 2 or len(new_user.first_name) > 254 or not LETTERS_REGEX.match(new_user.first_name):
            errors.append('First Name must be between two and 254 letters. No other characters allowed.')
        # Last Name - Required; No fewer than 2 characters; letters only
        if len(new_user.last_name) < 2 or len(new_user.last_name) > 254 or not LETTERS_REGEX.match(new_user.last_name):
            errors.append('Last Name must be between two and 254 letters. No other characters allowed.')
        # Bonus: Birthday field - before today
        if new_user.birthdate > now():
            errors.append('Birthdate must be in the past')
        # Email - Required; Valid Format
        if len(new_user.email) < 5 or not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email address')

        # TODO: password
        # Password - Required; 
        # No fewer than 8 characters in length; 
        # matches Password Confirmation

        if len(errors) > 0:
            return (False, errors)

        try:
            self.get(email=new_user.email)
            errors.append('That is not a valid email')
            return (False, errors)
        except:
            # TODO: encrypt the pw in here somewhere
            # TODO: send the pw to the DB, too!
            user = self.create(first_name=new_user.first_name, last_name=new_user.last_name, birthdate=new_user.birthdate, email=new_user.email)
            return (True, user)


    def login_validator(self, postData):
        errors = []
        user = user.id
        user.email = postData['email'] 
        user.password = postData['password']

        # TODO: email match
        # TODO: password match using bcrypt unhash magic
        pass


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=64)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
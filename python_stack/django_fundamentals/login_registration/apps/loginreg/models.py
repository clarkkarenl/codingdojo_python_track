# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from datetime import datetime

import bcrypt
from django.contrib.auth import authenticate, login
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        first_name = postData['first_name']
        last_name = postData['last_name']
        birthdate = postData['birthdate']
        email = postData['email'] 
        password = postData['password'] 
        confirm_pw = postData['confirm_pw']

        # First Name - Required; No fewer than 2 characters; letters only
        if len(first_name) < 2 or len(first_name) > 254 or not LETTERS_REGEX.match(first_name):
            errors.append('First Name must be between two and 254 letters. No other characters allowed.')
        # Last Name - Required; No fewer than 2 characters; letters only
        if len(last_name) < 2 or len(last_name) > 254 or not LETTERS_REGEX.match(last_name):
            errors.append('Last Name must be between two and 254 letters. No other characters allowed.')
        # Bonus: Birthday field - before today
        if datetime.strptime(birthdate, "%Y-%m-%d").strftime("%Y-%m-%d") >= datetime.strftime(datetime.now(), "%Y-%m-%d"):
            errors.append('Birthdate must be in the past')
        # Email - Required; Valid Format
        if len(email) < 5 or not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email address')

        if len(password) < 8:
            errors.append('Please enter a valid password')
        if password != confirm_pw:
            errors.append('Password does not match confirmation password')

        if len(errors) > 0:
            return (False, errors)

        try:
            self.get(email=email)
            errors.append('That is not a valid email')
            return (False, errors)
        except:
            hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            user = self.create(first_name=first_name, last_name=last_name, birthdate=birthdate, email=email,password=hashed_pw)
            return (True, user)


    def login_validator(self, postData):
        errors = []
        email = postData['email']
        password = postData['password']
        
        if not User.objects.get(email=email) or len(email) < 5:
            errors.append('Invalid email. Please try again.')
            return (False, errors)

        user = User.objects.get(email=email)

        if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
            user = User.objects.get(email=email)
            return (True, user)
        else:
            errors.append('An error occurred. Please try again.')
            return (False, errors)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=64)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

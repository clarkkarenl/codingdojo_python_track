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
        name = postData['name']
        alias = postData['alias']
        email = postData['email'] 
        password = postData['password'] 
        confirm_pw = postData['confirm_pw']

        # First Name - Required; No fewer than 2 characters; letters only
        if len(name) < 2 or len(name) > 254 or not LETTERS_REGEX.match(name):
            errors.append('First Name must be between two and 254 letters. No other characters allowed.')
        # Last Name - Required; No fewer than 2 characters; letters only
        if len(alias) < 2 or len(alias) > 254 or not LETTERS_REGEX.match(alias):
            errors.append('Last Name must be between two and 254 letters. No other characters allowed.')
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
            user = self.create(name=name, alias=alias, email=email,password=hashed_pw)
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
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)


class Review(models.Model):
    reviews = models.TextField()
    rating = models.IntegerField   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
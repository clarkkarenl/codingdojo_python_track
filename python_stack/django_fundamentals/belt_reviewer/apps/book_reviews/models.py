from __future__ import unicode_literals

import re
from datetime import datetime

import bcrypt
from django.contrib.auth import authenticate, login
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_REGEX = re.compile(r'^[a-zA-Z ]+$')


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        name = postData['name']
        alias = postData['alias']
        email = postData['email'] 
        password = postData['password'] 
        confirm_pw = postData['confirm_pw']

        if len(name) < 2 or len(name) > 254 or not LETTERS_REGEX.match(name):
            errors.append('Name must be between two and 254 letters.')
        if name[0] == " " or name[len(name) - 1] == " ":
            errors.append('Name cannot start or end with a space')
        # Last Name - Required; No fewer than 2 characters; letters only
        if len(alias) < 2 or len(alias) > 254 or not LETTERS_REGEX.match(alias):
            errors.append('Alias must be between two and 254 letters.')
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
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = self.create(name=name, alias=alias, email=email,password=hashed_pw)
            return (True, user)


    def login_validator(self, postData):
        errors = []
        email = postData['email']
        password = postData['password']

        try:
            self.get(email=email)
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                user = self.get(email=email)
                return (True, user)
            else:
                errors.append('An error occurred. Please try again.')
                return (False, errors)
        except:
            errors.append('Incorrect email or password. Please try again.')
            return (False, errors)


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_text = models.TextField()
    stars = models.CharField(max_length=1)   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.review_text

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import re

# Email - Required; Valid Format
# Password - Required; No fewer than 8 characters in length; matches Password Confirmation

def validate_name(value):
    letters = re.compile('[A-Za-z]+$')

    if letters.match(value) == None:
        raise ValidationError('Name must only contain letters')

    if len(value) < 2:
        raise ValidationError('Name must be longer than 2 characters')

def validate_password(value):

    if len(value) < 8:
        raise ValidationError('Password must contain 8 or more characters')




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    email = models.CharField(max_length=30, unique=True, )
    password = models.CharField(max_length=50, validators=[validate_password])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

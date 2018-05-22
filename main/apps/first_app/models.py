from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')

class UserManager(models.Manager):
    # inherit from the User class
    # possibility to send error messages
    # don't forget to connect with the views.py file to implement everything in the methods
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 3:
            errors['fname'] = 'Full name needs to have at least more then 3 characters'
        if len(postData['email']) < 1:
            errors['email'] = 'It needs to be a propper email address'
        elif not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = 'It needs to be a propper email address'
        return errors
        # return the errors otherwise it wouldn't return anything!!

class User(models.Model):
    fname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # with objects = UserManager() create the connection with the User class 
    objects = UserManager()
    def __repr__(self):
        return '<User object: {} {}'.format(self.fname, self.email)

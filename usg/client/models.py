from django.db import models
from django.contrib.auth.models import AbstractUser
# from firebase_admin import auth

class User:
        def __init__(self, email, password, name, phone):
                self.email = email
                self.password = password
                self.name = name
                self.phone = phone

        def fromJson(self, json):
                self.email = json['email']
                self.password = json['password']
                self.name = json['name']
                self.phone = json['phone']

        def toJson(self):
                return {
                        'email': self.email,
                        'password': self.password,
                        'name': self.name,
                        'phone': self.phone
                 }
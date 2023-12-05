from django.db import models
from django.contrib.auth.models import AbstractUser
# from firebase_admin import auth


class User:
    def __init__(self, email=None, password=None, name=None, phone=None):
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


class UserStory:
    def __init__(self, idUserStory=None, nameUserStory=None,ProjectTitle=None,inputParagraf=None,created_at=None):
        # self.idUserStory = idUserStory
        # self.nameUserStory = nameUserStory
        self.ProjectTitle= ProjectTitle
        self.inputParagraf= inputParagraf
        self.created_at = created_at

    def fromJson(self, json):
        # self.idUserStory = json['id']
        # self.nameUserStory = json['name']        
        self.ProjectTitle = json['ProjectTitle']
        self.inputParagraf = json['inputParagraf']
        self.created_at = json['created_at']

    def toJson(self):
        return {
            'ProjectTitle': self.ProjectTitle,
            'inputParagraf': self.inputParagraf,
            'created_at': self.created_at
        }


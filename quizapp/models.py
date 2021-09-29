from django.db import models
from django.db.models.fields import BigIntegerField, CharField, EmailField


class signup_form(models.Model):
    Name = CharField(max_length=20)
    Place = CharField(max_length=20)
    Email = CharField(max_length=20)
    Password = CharField(max_length=20)
    Re_password = CharField(max_length=20)
    Contact = BigIntegerField()

class admin_reg(models.Model):
    username = CharField(max_length=20)
    password = CharField(max_length=20)


class Quiz_question(models.Model):
    
    Questions = CharField(max_length=500)
    Category = CharField(max_length=30)
    Option_A = CharField(max_length=20)
    Option_B = CharField(max_length=20)
    Option_C = CharField(max_length=20)
    Option_D = CharField(max_length=20)
    Answer = CharField(max_length=20)


    

# Create your models here.

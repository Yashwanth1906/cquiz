from django.db import models

# Create your models here.

class questions(models.Model):
    qno = models.IntegerField()
    question = models.TextField(max_length=10000)
    choice1 = models.CharField(max_length=1000)
    choice2 = models.CharField(max_length=1000)
    choice3 = models.CharField(max_length=1000)
    choice4 = models.CharField(max_length=1000)
    anschoiceno = models.CharField(max_length=1000)

class details(models.Model):
    Name = models.CharField(max_length=100)
    RegisterNo = models.CharField(max_length=20)
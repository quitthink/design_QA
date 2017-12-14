from django.db import models

# Create your models here.
class list_t1s(models.Model):
    t1s = models.CharField(max_length=32)

class list_t1(models.Model):
    t1 = models.CharField(max_length=32)

class list_t3s(models.Model):
    t3s = models.CharField(max_length=32)

class list_t3(models.Model):
    t3 = models.CharField(max_length=32)
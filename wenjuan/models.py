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

class stu_record(models.Model):
    stu_name = models.CharField(max_length=32)
    stu_num = models.CharField(max_length=32)
    stu_sex = models.CharField(max_length=8)
    stu_class = models.CharField(max_length=32)
    game1 = models.CharField(max_length=8)
    game2 = models.CharField(max_length=8)
    game3 = models.CharField(max_length=8)
    game4 = models.CharField(max_length=8)
    game5 = models.CharField(max_length=8)
    game6 = models.CharField(max_length=8)
    SH_self_m= models.CharField(max_length=8)
    SH_allot_stu_a= models.CharField(max_length=32)
    SH_allot_stu_a_m=models.CharField(max_length=8)
    M_allot_stu_a = models.CharField(max_length=32)
    M_allot_stu_a_m= models.CharField(max_length=8)
    M_allot_stu_b = models.CharField(max_length=32)
    M_allot_stu_b_m = models.CharField(max_length=8)
    L_allot_stu_a = models.CharField(max_length=32)
    L_allot_stu_a_m = models.CharField(max_length=8)
    L_allot_stu_b = models.CharField(max_length=32)
    L_allot_stu_b_m = models.CharField(max_length=8)
    E_allot_stu_a = models.CharField(max_length=32)
    E_allot_stu_a_m = models.CharField(max_length=8)
    E_allot_stu_b = models.CharField(max_length=32)
    E_allot_stu_b_m = models.CharField(max_length=8)

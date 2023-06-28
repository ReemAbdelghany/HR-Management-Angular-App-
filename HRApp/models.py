from django.db import models


class Branch(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=255)
    b_building_no = models.CharField(max_length=255)
    b_st = models.CharField(max_length=255)
    b_area = models.CharField(max_length=255)
    b_city = models.CharField(max_length=255)
    b_country = models.CharField(max_length=255)
    b_manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=255)
    e_age = models.IntegerField()
    e_email = models.EmailField(max_length=255)
    e_phone_number = models.CharField(max_length=20)
    e_branch = models.ForeignKey('Branch', on_delete=models.CASCADE)



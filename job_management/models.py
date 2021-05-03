from django.db import models

# Create your models here.
from django.db.models import Model


class main_category(Model):
    main_category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.main_category_name


class sub_category(Model):
    main_category_name=models.CharField(max_length=200)
    sub_category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_category_name



class sub_sub_category(Model):
    main_category_name=models.CharField(max_length=200)
    sub_category_name=models.CharField(max_length=200)
    sub_sub_category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_sub_category_name



class Add_Job(Model):
    main_category_name = models.CharField(max_length=200)
    sub_category_name = models.CharField(max_length=200)
    sub_sub_category_name = models.CharField(max_length=200)
    jobname=models.CharField(max_length=200)
    startdate=models.DateField(max_length=200)
    lastdate=models.DateField(max_length=200)
    offlinedate=models.DateField(max_length=200)
    applylink=models.CharField(max_length=500)
    official_notification_link=models.CharField(max_length=500)
    official_website_link=models.CharField(max_length=500)
    def __str__(self):
        return self.jobname


class Manager(Model):
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
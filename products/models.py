from django.db import models


# Create your models here.sefd


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)


class Product(models.Model):
    company = models.ForeignKey('Company', related_name='company', blank=False, unique=False,
                                on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=100)


class Seller(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

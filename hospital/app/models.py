from django.db import models

# Create your models here.
class appointmenttable(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    depart = models.CharField(max_length=200)
    doc = models.CharField(max_length=200)
    message = models.CharField(max_length=200)


class contacttable(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

class registrationtable(models.Model):
    finame = models.CharField(max_length=200)
    laname = models.CharField(max_length=200)
    emaill = models.CharField(max_length=200)
    passwords = models.CharField(max_length=200)
    re_passwords = models.CharField(max_length=200)

#admin side

class adminregistertable(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ree_password = models.CharField(max_length=200)
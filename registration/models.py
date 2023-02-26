from django.db import models

# Create your models here.

class qrvalues(models.Model):
  qrtext = models.CharField(max_length=200)
  qrhash = models.CharField(max_length=300)


class participant(models.Model):
  fullname = models.CharField(max_length=200)
  registrationnumber = models.CharField(max_length=100)
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  branch = models.CharField(max_length=100)
  institute = models.CharField(max_length=100)
  campus = models.CharField(max_length=100)
  registrar = models.CharField(max_length=200)
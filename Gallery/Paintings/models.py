from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length = 50, null = True, default = None)

class Paintings(models.Model):
    type = models.CharField(max_length = 25, null = True, default = None)
    owner = models.ForeignKey(Owner, null = True)
    description = models.CharField(max_length = 200, null = True, default = None)

from django.db import models

class Member(models.Model):
  name = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  
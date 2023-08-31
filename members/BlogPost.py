from django.db import models

class Member(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_date = models.DateField(null=True)
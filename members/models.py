from django.db import models

class BlogPost(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_date = models.DateField(null=True)

class product(models.Model):
  name = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
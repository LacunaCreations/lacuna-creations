from django.db import models

class ContactMessageManager(models.Manager):
  def project_validator(self, postData):
    errors = {}
    return errors

class ContactMessage(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.TextField()
  message = models.CharField(max_length=200)

  objects = ContactMessageManager()
from __future__ import unicode_literals

from sre_constants import error
from turtle import title
from django.db import models

import re
import bcrypt
from django.http import request


##############################################################
# ADMIN VALIDATIONS
class AdministratorManager(models.Manager):
  # REGISTER VALIDATIONS 
  def register_validator(self, postData):
    errors = {}

    registration_code = "g3Eu0sVY3mtEkyE8m75EknpXG2k4h5"

    # NAME VALIDATIONS
    if len(postData['first_name']) < 2:
      errors['first_name'] = "First name must be at least two characters"
    if len(postData['last_name']) < 2:
      errors['last_name'] = "Last name must be at least two characters"

    # EMAIL VALIDATIONS
    email_regex = re.compile(r'^[a-zA-Z0-9.=_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(postData['email']) == 0:
      errors['email'] = "Email must be entered"
    elif not email_regex.match(postData['email']):
      errors['email'] = "Must be valid email"

    # PASSWORD VALIDATIONS
    if len(postData['password']) <= 3:
      errors['password'] = "Password must be entered"
    if postData['password'] != postData['conf_password']:
      errors['password_mismatch'] = "Passwords do not match"


    # CODE REGISTRATION
    if postData['code'] != registration_code:
      errors['code'] = "Invalid Registration Code"

    return errors

  # LOGIN VALIDATIONS 
  def login_validator(self, postData):
    errors = {}

    # EMAIL VALIDATIONS
    existing_user = Administrator.objects.filter(email = postData['email'])
    if len(existing_user) < 1:
      errors['email'] = "User does not exist"
    if not existing_user:
      errors['email'] = "No email entered"

    # PASSWORD VALIDATIONS
    if existing_user:
      if len(postData['password']) < 8:
        errors['password'] = "An eight character password must be entered"

    elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
        errors['mismatch'] = "Email and password"

    else:
      errors['No User'] = "Email and Password do not match"

    return errors
      
class EmployeeManager(models.Manager):
  def creation_validator(self, postData):
    errors = {}
    return errors

  def login_validator(self, postData):
    errors = {}
    return errors

class ProjectManager(models.Manager):
  def project_validator(self, postData):
    errors = {}
    return errors


class Administrator(models.Model):
  first_name = models.CharField(max_length = 15)
  last_name = models.CharField(max_length = 15)
  email = models.CharField(max_length = 50)
  username = models.CharField(max_length = 50, null=True, blank=True)
  phone = models.CharField(max_length=10, null=True, blank=True)
  title = models.CharField(max_length = 50, null=True, blank=True)
  password = models.CharField(max_length = 25)
  code = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  objects = AdministratorManager()

class Employee(models.Model):
  first_name = models.CharField(max_length = 15)
  last_name = models.CharField(max_length = 15)
  email = models.CharField(max_length = 50)
  password = models.CharField(max_length = 25)
  phone = models.CharField(max_length=10)
  creator = models.ForeignKey(Administrator, null=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  objects = EmployeeManager()

class Project(models.Model):
  project_name = models.CharField(max_length=200)
  company = models.CharField(max_length=200)
  description = models.TextField()
  client = models.CharField(max_length=200)
  service = models.CharField(max_length=200)
  price = models.CharField(max_length=200)
  creator = models.ForeignKey(Administrator, null=True, on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add = True)
  end_time = models.DateTimeField(auto_now = True)

  objects = ProjectManager()

class Project(models.Model):
  company_name = models.CharField(max_length=200)
  phone = models.CharField(max_length = 50)
  email = models.CharField(max_length=200)
  contact_name = models.CharField(max_length=200)
  creator = models.ForeignKey(Administrator, null=True, on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add = True)
  end_time = models.DateTimeField(auto_now = True)

  objects = ProjectManager()

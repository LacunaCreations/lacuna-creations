from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render, redirect, HttpResponse
from django.template import context

from .models import *

##############################################################
# ADMIN LOGIN
def admin_login(request):
  return render(request, 'admin_login.html')

def admin_login_logic(request):
  if request.method == 'POST':
    errors = Administrator.objects.login_validator(request.POST)
    
    # Check for login errors
    if errors:
      for e in errors.values():
        messages.error(request, e)
      print(errors)
      return redirect('/admin/login')

    # Log the user in
    logged_user = Administrator.objects.filter(email = request.POST['email'])

    request.session['admin_id'] = logged_user[0].id
    return redirect('/admin/dashboard')
  
  else:
    return redirect('/admin/login')

##############################################################
# ADMIN REGISTRATION
def admin_registration(request):
  return render(request, 'admin_registration.html')

def admin_registration_logic(request):
  if request.method == 'POST':
    errors = Administrator.objects.register_validator(request.POST)

    # Check for registeration errors
    if errors:
      for e in errors.values():
        messages.error(request, e)
      print(errors)
      return redirect('/admin/registration')

    # Create the new user
    hashed_pw = bcrypt.hashpw(
      request.POST['password'].encode(), bcrypt.gensalt()).decode()

    if request.POST['password'] == request.POST['conf_password']:

      new_admin = Administrator.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw,
        code = request.POST['code'],
      )
      request.session['admin_id'] = new_admin.ids

      return redirect('/admin/dashboard')

  return redirect('/admin/registration')

##############################################################
# ADMIN CREATE EMPLOYEE
def employee_registration(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    context = {
      'admin': logged_admin
    }
    return render(request, 'admin_create_employee.html', context)
  else:
    return redirect('/admin/login')

def employee_registration_logic(request):
  if request.method == 'POST':
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])

    errors = Employee.objects.creation_validator(request.POST)

    # Check for registeration errors
    if errors:
      for e in errors.values():
        messages.error(request, e)
      print(errors)
      return redirect('/admin/employee-registration')

    # Create the new user
    hashed_pw = bcrypt.hashpw(
      request.POST['password'].encode(), bcrypt.gensalt()).decode()

    if request.POST['password'] == request.POST['conf_password']:

      new_employee = Administrator.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw,
        phone = request.POST['phone'],
        creator = logged_admin,
      )

      request.session['employee_id'] = new_employee.id
      return redirect('/admin/dashboard')

  return redirect('/admin/settings')

##############################################################
# ADMIN DASHBOARD
def admin_dashboard(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    context = {
      'admin': logged_admin
    }
    print(logged_admin.first_name)
    print(logged_admin.last_name)
    return render(request, 'admin_dashboard.html', context)
  else:
    return redirect('/admin/login')
  
##############################################################
# ADMIN SETTINGS
def admin_settings(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    context = {
      'admin': logged_admin
    }
    return render(request, 'admin_settings.html', context)
  else:
    return redirect('/admin/login')

def admin_profile_update(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    context = {
      'admin': logged_admin
    }
    return render(request, 'admin_profile_update.html', context)
  else:
    return redirect('/admin/login')

def admin_profile_update_logic(request):
  if 'admin_id' in request.session:
    if request.method == 'POST':
      logged_admin = Administrator.objects.get(id = request.session['admin_id'])
      logged_admin.first_name = request.POST['first_name']
      logged_admin.last_name = request.POST['last_name']
      logged_admin.email = request.POST['email']
      logged_admin.username = request.POST['username']
      logged_admin.phone = request.POST['phone']
      logged_admin.title = request.POST['title']
      logged_admin.save()

    return redirect('/admin/admin-profile-update')
  else:
    return redirect('/admin/login')

    
##############################################################
# ADMIN UPDATE
def admin_update(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    context = {
      'admin': logged_admin
    }
    return render(request, 'admin_update.html', context)
  else:
    return redirect('/admin/login')

def admin_update_logic(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    
    logged_admin.name = request.POST['name']
    logged_admin.email = request.POST['name']
    logged_admin.password = request.POST['name']
    logged_admin.save()

    return redirect('/admin/settings')
  else:
    return redirect('/admin/login')

##############################################################
# ADMIN LOGOUT
def admin_logout(request):
  request.session.flush()
  return redirect('/admin/login')

##############################################################
# PROJECT
def projects(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    all_projects = Project.objects.all()
    context = {
      'projects': all_projects,
      'admin': logged_admin,
    }
    return render(request, 'projects.html', context)

  elif 'employee_id' in request.session:
    logged_employee = Employee.objects.get(id = request.session['employee_id'])
    all_projects = Project.objects.all()
    context = {
      'projects': all_projects,
      'employee': logged_employee,
    }
    return render(request, 'projects.html', context)

  else:
    return redirect('/admin/login')

def create_project(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    all_projects = Project.objects.all()
    context = {
      'projects': all_projects,
      'admin': logged_admin,
    }
    return render(request, 'create_project.html', context)

  else:
    return redirect('/admin/login')

def create_project_logic(request):
  if 'admin_id' in request.session:
    if request.method == 'POST':
      logged_admin = Administrator.objects.get(id = request.session['admin_id'])
      new_project = Project.objects.create(
          project_name = request.POST['project_name'],
          company = request.POST['company'],
          description = request.POST['description'],
          client = request.POST['client'],
          service = request.POST['service'],
          price = request.POST['price'],
          creator = logged_admin,
        )
      return redirect('/admin/projects')

  else:
    return redirect('/admin/login')

def delete_project(request, project_id):
  if 'admin_id' in request.session:
    this_project = Project.objects.get(id = project_id)
    this_project.delete()
    return redirect('/admin/projects')

  else:
    return redirect('/admin/login')

##############################################################
# CLIENTS
def clients(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    all_clients = Client.objects.all()
    context = {
      'clients': all_clients,
      'admin': logged_admin
    }
    return render(request, 'clients.html', context)
  
  else:
    return redirect('/admin/login')
  
def create_client(request):
  if 'admin_id' in request.session:
    logged_admin = Administrator.objects.get(id = request.session['admin_id'])
    all_clients = Client.objects.all()
    context = {
      'clients': all_clients,
      'admin': logged_admin,
    }
    return render(request, 'create_client.html', context)

  else:
    return redirect('/admin/login')

def create_client_logic(request):
  if 'admin_id' in request.session:
    if request.method == 'POST':
      logged_admin = Administrator.objects.get(id = request.session['admin_id'])
      new_client = Client.objects.create(
          company_name = request.POST['company_name'],
          contact_name = request.POST['contact_name'],
          phone = request.POST['phone'],
          email = request.POST['email'],
          creator = logged_admin,
        )
    return redirect('/admin/clients')

  else:
    return redirect('/admin/clients')

def delete_client(request, client_id):
  if 'admin_id' in request.session:
    this_client = Client.objects.get(id = client_id)
    this_client.delete()
    return redirect('/admin/clients')

  else:
    return redirect('/admin/login')



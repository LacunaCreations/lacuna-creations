from email import message
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django import forms

from django.template.loader import render_to_string

from django.conf import settings
from .models import *

def index (request):
  return render(request, 'dev-index.html')
  # return render(request, 'index.html')

def home_page (request):
  return render(request, 'index.html')

def team_page (request):
  return render(request, 'team.html')

def about_page (request):
  return render(request, 'about.html')

def contact_page (request):
  return render(request, 'contact.html')

def portfolio_page (request):
  return render(request, 'portfolio.html')

def services_page (request):
  return render(request, 'services.html')

def contact_message_logic(request):
  if request.method == 'POST':
    new_contact_message = ContactMessage.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      phone = request.POST['phone'],
      message = request.POST['message'],
    )

    merge_data = {
      'message': new_contact_message,
    }

    email_body = render_to_string("page_items/email_template.html", merge_data)

    msg = EmailMultiAlternatives(
      'New Contact Inquiry', 
      email_body,
      to=['contact@lacunacreations.com']
    )

    msg.attach_alternative(email_body, 'text/html')
    msg.send()
    print('Email Sent')
    
    messages.success(request, 'Form Submitted')

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
  else:
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


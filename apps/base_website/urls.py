from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('team', views.team_page),
  path('about', views.about_page),
  path('contact', views.contact_page),
  path('portfolio', views.portfolio_page),
  path('services', views.services_page),

  path('contact-message', views.contact_message_logic),

]
from django.urls import path
from . import views

urlpatterns = [
  path('login', views.admin_login),
  path('login-logic', views.admin_login_logic),
  path('registration', views.admin_registration),
  path('registration-logic', views.admin_registration_logic),

  path('settings', views.admin_settings),
  path('admin-profile-update', views.admin_profile_update),
  path('admin-profile-update-logic', views.admin_profile_update_logic),

  path('projects', views.projects),

  path('logout', views.admin_logout),

  path('dashboard', views.admin_dashboard),
]
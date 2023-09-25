from django.urls import path
from . import views

urlpatterns = [
  path('login', views.admin_login),
  path('login-logic', views.admin_login_logic),
  path('registration', views.admin_registration),
  path('registration-logic', views.admin_registration_logic),

  # Admin Settings
  path('settings', views.admin_settings),
  path('admin-profile-update', views.admin_profile_update),
  path('admin-profile-update-logic', views.admin_profile_update_logic),

  # Projects
  path('projects', views.projects),
  path('create-project', views.create_project),
  path('create-project-logic', views.create_project_logic),
  path('delete-project/<int:product_id>', views.delete_project),

  # Logout
  path('logout', views.admin_logout),

  # Dashboard
  path('dashboard', views.admin_dashboard),
]
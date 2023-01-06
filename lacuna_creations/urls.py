from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('apps.base_website.urls')),
    path('admin/', include('apps.admin_dashboard.urls')),

]

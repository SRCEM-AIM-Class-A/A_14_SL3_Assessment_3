from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_view  # Import the default view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('documents/', include('documents.urls')),
    path('', dashboard_view, name='home'),  # Root URL directs to dashboard
]

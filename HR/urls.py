from django.contrib import admin
from django.urls import path
from HRApp.views import branchApi, employeeApi


urlpatterns = [
    path('branches/', branchApi),  # Endpoint for managing branches
    path('branches/<int:id>/', branchApi),  # Endpoint for specific branch by ID
    path('employees/', employeeApi),  # Endpoint for managing employees
    path('employees/<int:id>/', employeeApi),  # Endpoint for specific employee by ID
    path('admin/', admin.site.urls),
]

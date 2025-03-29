from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'ewaste_app'

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # Dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Report URLs
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/', views.report_list, name='report_list'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_acc,name='login'),
    path('register/',views.signup_acc,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
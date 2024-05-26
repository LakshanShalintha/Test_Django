from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('signup/', views.signup, name='signup'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('login/', views.login, name='login'),
]

from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('register', views.register, name='register'),
  path('savedetails', views.savedetails, name='savedetails'),
  path('verify', views.verify, name='verify'),
  path('verifydetails', views.verifydetails, name='verifydetails'),
]

handler404 = "registration.views.page_not_found_view"

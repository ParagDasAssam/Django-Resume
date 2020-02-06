from django.urls import path

from my_resume import views

urlpatterns = [
    path('', views.home, name='home'),
]
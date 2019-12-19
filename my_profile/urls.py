from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.my_style, name='my_style'),
    path('linkedin/',views.linkedin,name = 'linkedin'),
    path('resume/',views.resume,name='resume'),
    path('one_slider/',views.one_slider,name='slider'),
    path('poster/',views.poster,name='poster'),
    path('contact/',views.contact,name='contact'),
    path('',views.animation,name='animation'),
]
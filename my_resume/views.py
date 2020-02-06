from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import webbrowser

def home(request):
    return render(request,'my_resume/index.html',{})
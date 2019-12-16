from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import webbrowser

def my_style(request):
    template = loader.get_template('my_profile/my_resume/index.html')
    return HttpResponse(template.render())
def linkedin(request):
    webbrowser.open("www.linkedin.com/in/parag-das")
    return render(request,'my_profile/my_resume/index.html',{}) 
def animation(request):
    return render(request,'my_profile/my_resume/animation.html',{})
def resume(request):
    return render(request,'my_profile/my_resume/resume.html',{})
def one_slider(request):
    return render(request,'my_profile/my_resume/one_slider.html',{})
def poster(request):
    return render(request,'my_profile/my_resume/poster.html',{})
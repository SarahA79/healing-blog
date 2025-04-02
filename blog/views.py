from django.shortcuts import render

from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("<h1>Welcome to the Healing Blog</h1>")

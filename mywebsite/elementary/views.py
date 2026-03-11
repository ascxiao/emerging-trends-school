from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "elementary.html")

def about(request):
    return render(request, "about_elementary.html")

# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')
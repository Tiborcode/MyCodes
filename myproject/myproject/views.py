from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
import os


def home(request):
    return render(request, 'home.html')

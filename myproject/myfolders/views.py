from django.shortcuts import render


# Create your views here.
def myfolders(request):
    return render(request, 'myfolders/myfolders.html')

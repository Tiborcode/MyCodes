from django.shortcuts import render, HttpResponse
from .forms import UploadFilesForm
from .models import Files

# Create your views here.
def myfolders(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)
        uploaded_file = request.FILES['file'] #'file' refers to variable defined in forms.py
        new_file = Files.objects.create(file=uploaded_file)
        new_file.save()
        return HttpResponse("the id of file is" + str(new_file.pk))

    else:
        form = UploadFilesForm()
    return render(request, 'myfolders/myfolders.html', {'form': form})


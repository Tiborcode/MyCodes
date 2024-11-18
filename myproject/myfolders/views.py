from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .forms import UploadFilesForm
import os
from .models import Files


# Create your views here.
# def upload_file(request):
#     if request.method == "POST":
#         form = UploadFilesForm(request.POST, request.FILES)
#         uploaded_file = request.FILES[
#             'file']  #'file' refers to variable defined in forms.py, FILES['file'] points to a dict item with key of 'file'
#         fs = FileSystemStorage(location='uploads/')
#         fs.save(uploaded_file.name, uploaded_file)
#         # new_file = Files.objects.create(file=uploaded_file)
#         # id_num = new_file.pk
#         # print(id_num)
#         # new_file.save()
#         return redirect('myfolders:upload')
#
#     else:
#         form = UploadFilesForm()
#     return render(request, 'myfolders/myfolders.html', {'form': form})


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        try:
            files = request.FILES.getlist('files')
            fs = FileSystemStorage(location='uploads/')
            for file in files:
                fs.save(file.name, file)
            return JsonResponse({'status': 'success', 'message': 'Files uploaded successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        form = UploadFilesForm()
    return render(request, 'myfolders/myfolders.html', {'form': form})

def delete_file(request, filename):
    file_path = os.path.join('uploads/', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return JsonResponse({'status': 'success', 'message': 'File deleted successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)

def list_files(request):
    files = Files.objects.all()
    return render(request, 'myfolders/file_list.html', {'files': files})
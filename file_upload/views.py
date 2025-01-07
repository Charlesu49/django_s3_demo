from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload:upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload_file.html', {'form': form})

def upload_success(request):
    return render(request, 'file_upload/upload_success.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadForm
from .models import UserFiles

def index_page_view(request):
    form = UploadForm()
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        
            messages.success(request, 'File uploaded successfully.')
            return redirect('index')
    
    user_files = UserFiles.objects.all()
    context = {'form': form, 'uploaded_files': user_files}
    return render(request, 'uploader/index.html', context)
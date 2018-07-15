from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage


def homeFace(request):
    return render(request, 'home_face.html')


def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'uimage.html', {'form': form})

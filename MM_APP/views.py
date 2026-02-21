from django.shortcuts import render, redirect
from .models import Mediacontent
from .forms import MediaContentForm


def home(request):
    contents = Mediacontent.objects.all()
    return render(request, 'MM_APP/home.html', {'contents': contents})


def upload(request):
    if request.method == 'POST':
        form = MediaContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaContentForm()

    return render(request, 'MM_APP/upload.html', {'form': form})


def about(request):
    return render(request, 'MM_APP/about.html')
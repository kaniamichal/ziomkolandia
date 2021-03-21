from django.forms import forms, ModelForm
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import KidsEnroll


def index(request):
    return render(request, 'website/index.html')


def kids_enroll(request):
    if request.method == "POST":
        form = KidsEnroll(request.POST)
        if form.is_valid():
            kindergarten = form.save(commit=False)
            kindergarten.data_enrol = timezone.now()
          #  kindergarten.regulations(required=True)
            kindergarten.save()
            return redirect('thanks')
    else:
        form = KidsEnroll()
    return render(request, 'website/przedszkola.html', {'form': form})


def thanks(request):
    return render(request, 'website/thanks.html')
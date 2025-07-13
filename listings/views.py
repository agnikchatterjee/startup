from django.shortcuts import render
from .models import Accommodation

def home(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'listings/index.html', {'accommodations': accommodations})


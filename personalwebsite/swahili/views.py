from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def mambo_dunia(request):
    return render(request, 'swahili/index.html', {})






from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello, world. You're at the overview index.")

def hello_world(request):
    return render(request, 'index_test.html', {})
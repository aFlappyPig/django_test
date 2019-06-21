from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Teacher


# Create your views here.

def index(request):
    data = Teacher.objects.all()
    return render(request, template_name='home.html', context={'teachers': data})


def query_teacher(request):
    return HttpResponse('no teacher')


def test(request):
    return redirect('../')

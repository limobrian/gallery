from django.shortcuts import render,redirect
from django import HttpResponse, Http404
from .models import image

# Create your views here.


def gallery (request):
    all_pic = Image.all_pics()
    print(all_pic)
    return render(request,'gallery.html',{"all_pic":all_pic})


from django.shortcuts import render, redirect
from Newsapp import views
from django.http import HttpResponse
#from .forms import *
#from Newsapp import form




def Homepage(request):

    return render(request,'Newsapp/Home.html')


def indexpage(request):
    return render(request,'Newsapp/index.html')

"""def firenews(request):
    if request.method == 'POST':
        form = News11Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('success')
    else:
        form = News11Form()
    return render(request, 'Newsapp/newsfire.html' , {'form' : form})"""

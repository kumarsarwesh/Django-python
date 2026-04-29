''' 
from django.shortcuts import render

# Create your views here.
'''
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('Welcome to django home page !')
    return render(request,'index.html')




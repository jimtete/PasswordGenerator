from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    letters = list('abcdefghijklmnopqrstuvwxyz')

    if (request.GET.get('uppercase')):
        letters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if (request.GET.get('special')):
        letters.extend("$@!)(*&^%#_-+=?")
    if (request.GET.get('numbers')):
        letters.extend("0123456789")

    length=int (request.GET.get('length', 12))

    

    thePassword=''
    for i in range(length):
        thePassword += random.choice(letters)


    return render(request, 'generator/password.html', {'password':thePassword})
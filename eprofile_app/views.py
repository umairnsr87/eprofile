from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'index.html',{})


def details(request):
    if request.method=='POST':
        phone = str( request.POST.get( "phone" ) )
        print( "This is the phone number" + str( phone ) )
    return render(request,'details.html',{})

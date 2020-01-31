from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import  login_required
from .models import resume


# Create your views here.
def home(request):
    return render(request,'index.html',{})


def details(request):
    if request.method=='POST':
        phone = str( request.POST.get( "phone" ) )
        print( "This is the phone number" + str( phone ) )
    return render(request,'details.html',{})

@login_required
def create_resume(request):
    if request.method=="POST":
        phone=request.POST.get("phone")
        country=request.POST.get("country")
        city=request.POST.get("city")
        resume1=resume(user_id=request.user.id,phone=phone,country=country,city=city)
        resume1.save()
        messages.success( request, f'Your Account is updated !' )


    print("This is the login user"+str(request.user))
    #print(user.username)
    return render(request,'create-resume.html',{})
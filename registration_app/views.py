from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def Registeruser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('/')
            else:

                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                return redirect('login')
        else:
            messages.info(request,"Password is not matched")
            return redirect('/')

    return render(request,'account/register.html')

def loginuser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('userdisplay')
        else:
            messages.info(request,"please enter valid details")
            return redirect('login')
    return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def homepage(request):
    auth.login(request)
    return redirect('userdisplay')


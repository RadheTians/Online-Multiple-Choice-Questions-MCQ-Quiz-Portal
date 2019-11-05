from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from exam.models import Question,Clock


# Create your views here.

def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        psw = request.POST['psw'] 
        rep_psw = request.POST['psw_repeat']
        if psw == rep_psw:
            if User.objects.filter(username=username):
                return render(request,'register.html',{'message' : 'Username is already taken.'})
            elif User.objects.filter(email=email):
                return render(request,'register.html',{'message' : 'Email Id is already taken.'})
            else :
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=psw)
                user.save()
                return render(request,'login.html')
        else:
            return render(request,'register.html',{'message' : 'Password is not matching.'})
       
    else:
        return render(request,'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            clock = Clock.objects.all()
            if clock[0].flag :
                return render(request,'home.html')
            else:
                return render(request,'login.html',{'message' : "You cann't start test, because admin isn't started exam yet."})
        else:
            return render(request,'login.html',{'message' : "Invaild User or Password isn't correct."})
    else:
        return render(request,'login.html',{'message' : "Post Request Error."})
    

def Logout(request):
    auth.logout(request)
    return render(request,'login.html')






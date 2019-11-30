from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def sign_up(request):
    if request.method=="POST":
        #the user wants to sign up after entering their information
        if request.POST['password1']=="" or request.POST['username']=="":
            return render(request,"accounts/sign_up.html",{'error':"must enter all fields"})
        elif request.POST['password1']==request.POST['password2']: # everything used here is referenced in sign_up.html 
                                                                 # under the form tag and is called using name given
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,"accounts/sign_up.html",{'error':"username is already taken"})
            except User.DoesNotExist: # condition for if user doesn't exist and the passwords entered match
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,"accounts/sign_up.html",{'error':"passwords enter do not match"})
    else:
        #user wants to enter info
        return render(request,"accounts/sign_up.html")
def login(request):
    if request.method=="POST":
        print (request.body)
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,"accounts/login.html",{'error':"username or password incorrect"})
    else:
        return render(request,"accounts/login.html")
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
    return render(request,"accounts/sign_up.html")
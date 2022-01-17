from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def acc(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    return render(request, 'blog/acc.html')

def sign_up(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1!=pass2:
            messages.error(request, "Passwords doesn't match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, " Your eCoder has been successfully created")
            return redirect('home')

    return render(request, 'blog/signup.html')

def log_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
        else:
            messages.error(request, "Invalid credentials! Please try again.")
    
    return redirect('home')

def log_out(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
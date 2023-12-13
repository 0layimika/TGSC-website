from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            try:
                User.objects.get(email=request.POST["email"])
                return render(request,'account/signup.html', {'error':'Email already exists'})
            except User.DoesNotExist:
                try:
                    User.objects.get(username=request.POST["username"])
                    return render(request,'account/signup.html',{'error':'Username not available'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password2'],email=request.POST['email'])
                    auth.login(request, user)
                    return redirect('home')
        else:
            return render(request, 'account/signup.html',{'error':'passwords do not match'})
    else:
        return render(request,'account/signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'account/signup.html')





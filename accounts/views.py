from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
    else:
        form  = RegisterForm()

    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request,'accounts/login.html',{'error': 'Invalid credentials' })
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    return render(request,'accounts/profile.html')

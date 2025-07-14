from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from posts.models import Posts
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
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
    user_posts = Posts.objects.filter(user=request.user).order_by('-created_at')
    posts_count = len(user_posts)
    return render(request,'accounts/profile.html',{'user_posts':user_posts , 'posts_count':posts_count})


@login_required(login_url='login')
def edit_profile(request):
    profile,_ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'accounts/edit_profile.html',{'form':form})

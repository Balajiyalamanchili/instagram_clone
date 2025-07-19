from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from posts.models import Posts


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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
def show_user_profile(request,username):
    user = get_object_or_404(User, username=username)
    user_posts = Posts.objects.filter(user=user).order_by('-created_at')
    posts_count = len(user_posts)
    return render(request,'accounts/show_user_profile.html',{'user_posts':user_posts , 'posts_count':posts_count, 'user':user})

@login_required(login_url='login')
def follow_unfollow(request,follow_id):
    current_user = request.user
    current_user_profile = Profile.objects.get(user=current_user)

    target_user = User.objects.get(id=follow_id)
    target_user_profile = Profile.objects.get(user=target_user)


    if current_user in target_user_profile.followers.all():
        target_user_profile.followers.remove(current_user)
        current_user_profile.following.remove(target_user)
    else:
        target_user_profile.followers.add(current_user)
        current_user_profile.following.add(target_user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
    # return redirect('show_user_profile', username=target_user_profile.user)


# def like_post(request, post_id):
#     post = Posts.objects.get(id=post_id)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#         print(f"{request.user} unliked the post",post.likes,post.id)
#     else:
#         post.likes.add(request.user)
#         print(f"{request.user} liked the post")
#     return redirect('show_posts')




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


from django.http import JsonResponse, HttpResponseServerError
import logging

logger = logging.getLogger(__name__)


# @login_required(login_url='login')
# def show_all_users(request):
#     try:
#         # Test line to simulate an exception
#         raise Exception("Test exception for review")
#         all_users = User.objects.all()
#         return render(request, 'accounts/show_all_users.html', {'all_users': all_users}, status=200)
#     except Exception as e:
#         logger.error(f"Error fetching users: {str(e)}")
#         return HttpResponseServerError("Internal Server Error. Please try again later.")




@login_required(login_url='login')
def show_all_users(request):
    try:
        # raise Exception("Test exception")
        all_users = User.objects.all()
        return render(request, 'accounts/show_all_users.html', {'all_users': all_users})
    except Exception as e:
        error_message = "Something went wrong while loading users. Pls reload the page."
        return render(request, 'accounts/show_all_users.html', {
            'all_users': [],
            'error_message': error_message
        })




# using to active my website fake ping
from django.http import HttpResponse

def ping_view(request):
    return HttpResponse("pong")

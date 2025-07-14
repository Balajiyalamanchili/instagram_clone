from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Posts
# Create your views here.

def show_posts(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request,'posts/show_posts.html',{'posts':posts})



@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request,'posts/create_post.html',{'form': form})




@login_required
def like_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('show_posts')
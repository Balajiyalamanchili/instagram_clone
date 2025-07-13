from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.

def show_posts(request):
    return render(request,'posts/show_posts.html')


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

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentsForm
from .models import Posts

#ajax like try
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def show_posts(request):
    posts = Posts.objects.all().order_by('-created_at')
    comment_form = CommentsForm()
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Posts, id=post_id)
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('show_posts')

    return render(request,'posts/show_posts.html',{'posts':posts,'comment_form':comment_form})



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




# @login_required(login_url='login')
# def like_post(request, post_id):
#     post = Posts.objects.get(id=post_id)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#         print(f"{request.user} unliked the post",post.likes,post.id)
#     else:
#         post.likes.add(request.user)
#         print(f"{request.user} liked the post")
#     return redirect('show_posts')

#ajax like trail
@require_POST
@login_required
def like_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    user = request.user

    liked = False
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count(),
    })


# @login_required(login_url='login')
# def delete_post(request,post_id):
#     post = Posts.objects.get(id=post_id)
#     post.delete()
#     return redirect('profile')

@login_required(login_url='login')
def delete_post(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        post.delete()
    except Posts.DoesNotExist:
        pass  # Post already deleted or doesn't exist
    return redirect('profile')

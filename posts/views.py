from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def posts(request):
    posts = Post.objects.all().order_by('-created_at')    
    return render(request, 'posts/posts.html', {"posts": posts} )


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("posts:posts")



    return render(request, 'posts/createpost.html', {"form":form} )   
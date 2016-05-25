from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm, CommentForm

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_list')
    else :
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form' : form,
    })

def comment_new(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_new.html', {
        'form': form
    })

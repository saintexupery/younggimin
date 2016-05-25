from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

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
            return redirect('blog.views.post_list')
    else :
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form' : form,
    })
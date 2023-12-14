from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import *
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def home(request):
    blogs = Blog.objects
    latest_blog = Blog.objects.order_by('date_created')[:3]
    return render(request, 'blog/home.html', {'blogs': blogs,'latest_blog':latest_blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(post=blog)
    return render(request, 'blog/detail.html', {'blog': blog, 'comments':comments})
@login_required(login_url='/account/login')
def add_comment(request, blog_id):
    specific = get_object_or_404(Blog,pk=blog_id)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = specific
            comment.author = request.user
            comment.save()
            return redirect('detail', blog_id=blog_id)
        else:
            form = CommentForm()
    return render(request, 'blog/add_comment.html', {'blog': specific, 'form': form})
def all(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all.html', {'blogs': blogs})

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')
@login_required(login_url='/account/login')
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.user in blog.like.all():
        blog.like.remove(request.user)
        liked = False
    else:
        blog.like.add(request.user)
        liked = True

    return JsonResponse({'liked':liked, 'count':blog.like.count()})




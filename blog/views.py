from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate

from .forms import PostForm
from karyawan.models import Akun, Karyawan

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return render(request, 'blog/post_detail.html', {'post': post})
	else:
		form = PostForm()
	return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def appetizer(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'new/appetizer.html', {'posts': posts})
	
def maincourse(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'new/maincourse.html', {'posts': posts})
	
def dessert(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'new/dessert.html', {'posts': posts})
	
def hapus(request, pk):
	post = get_object_or_404(Post, pk=pk)
	categories = post.categories
	post.delete()
	return redirect('blog:'+categories)
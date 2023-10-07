from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AppLogin.models import Follow
from AppPost.models import Post, Like
# Create your views here.
@login_required
def home(req):
    following_list = Follow.objects.filter(follower=req.user)
    post = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(author=req.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    if(req.method == 'GET'):
        search = req.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)

    return render(req, 'AppPost/home.html', context={'search':search, 'result':result, 'list':following_list, 'posts': post, 'already_liked':liked_post_list})
@login_required
def liked(req, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, author=req.user)
    if not already_liked:
        like = Like(author=req.user, post=post)
        like.save()
    return HttpResponseRedirect(reverse('home'))
@login_required
def unliked(req, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, author=req.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
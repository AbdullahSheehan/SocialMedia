from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import UserProfile, Follow
from AppPost.forms import PostForm
# Create your views here.
def signUp(req):
    form = CreateNewUser()
    registered = False
    if(req.method == 'POST'):
        form = CreateNewUser(req.POST)
        if(form.is_valid()):
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('AppLogin:login'))
    return render(req, 'AppLogin/register.html', context={'form':form, 'status':registered})
def loginUser(req):
    form = AuthenticationForm()
    if(req.method == 'POST'):
        form = AuthenticationForm(data=req.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(req, user)
                return HttpResponseRedirect(reverse('home'))
    return render(req, 'AppLogin/login.html', context={'form':form})
@login_required
def profile(req):
    cur_user = UserProfile.objects.get(user=req.user)
    form = Profile(instance=cur_user)
    if(req.method == 'POST'):
        form = Profile(req.POST, req.FILES, instance=cur_user)
        if(form.is_valid()):
            form.save()
            form = Profile(instance=cur_user)
            return HttpResponseRedirect(reverse('AppLogin:myProfile'))
    return render(req, 'AppLogin/profile.html', context={'form':form})

@login_required
def logoutUser(req):
    logout(req)
    return HttpResponseRedirect(reverse('AppLogin:login'))

@login_required
def myprofile(req):
    form = PostForm()
    if(req.method == 'POST'):
        form = PostForm(req.POST, req.FILES)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.author = req.user
            obj.save()
            return HttpResponseRedirect(reverse('home'))
    return render (req,'AppLogin/myprofile.html', context={'form':form})

@login_required
def user(req, username):
    user = User.objects.get(username=username)
    already_follow = Follow.objects.filter(following=user, follower=req.user)
    if(user == req.user):
        return HttpResponseRedirect(reverse('AppLogin:myProfile'))
    return render(req, 'AppLogin/user_other.html', context={'user_other':user, 'already_follow':already_follow})

@login_required
def follow(req, username):
    following_user = User.objects.get(username= username)
    follower_user = req.user
    already_follow = Follow.objects.filter(following= following_user, follower=follower_user)
    if not already_follow:
        followedUser = Follow(follower = follower_user, following=following_user)
        followedUser.save()
    return HttpResponseRedirect(reverse('AppLogin:user', kwargs={'username':username}))

@login_required
def unfollow(req, username):
    following_user = User.objects.get(username= username)
    follower_user = req.user
    already_follow = Follow.objects.filter(following= following_user, follower=follower_user)
    already_follow.delete()
    return HttpResponseRedirect(reverse('AppLogin:user', kwargs={'username':username}))
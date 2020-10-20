from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, authenticate
from django.conf.urls.static import static
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html',  {"all_images": all_images, "all_users":all_users})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'insta/location.html', {'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'display/eplore.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'display/explore.html', {"message": message})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/userprofile.html')

def logout(request):
    return render(request, 'registration/logout.html')

def login(request):
    return render(request, 'display/home.html')


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'display/home.html', {"form": form})

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/login.html', {'form': form})

def UserProfile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)
	url_name = resolve(request.path).url_name
	
	if url_name == 'profile':
		posts = Post.objects.filter(user=user).order_by('-posted')

	else:
		posts = profile.favorites.all()

	#Profile info box
	posts_count = Post.objects.filter(user=user).count()
	following_count = Follow.objects.filter(follower=user).count()
	followers_count = Follow.objects.filter(following=user).count()

	#follow status
	follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

	#Pagination
	paginator = Paginator(posts, 8)
	page_number = request.GET.get('page')
	posts_paginator = paginator.get_page(page_number)

	template = loader.get_template('profile.html')

	context = {
		'posts': posts_paginator,
		'profile':profile,
		'following_count':following_count,
		'followers_count':followers_count,
		'posts_count':posts_count,
		'follow_status':follow_status,
		'url_name':url_name,
	}

	return HttpResponse(template.render(context, request))
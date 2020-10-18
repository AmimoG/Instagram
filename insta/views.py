from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html',  {"all_images": all_images}, {"all_users":all_users})


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
        return render(request, 'insta/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'insta/search_results.html', {"message": message})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/userprofile.html')

def logout(request):
    return render(request, 'registration/logout.html')

def login(request):
    return render(request, 'registration/login.html')

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
    return render(request, 'display/upload.html', {"form": form})

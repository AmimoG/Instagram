from django.shortcuts import render, redirect
from .models import Image, Comments, Profile
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

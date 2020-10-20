from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect

app_name = 'insta'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'profile',views.profile,name ='profile'),
    url(r'login',views.login,name ='login'),
    url(r'logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
    url(r'upload',views.upload,name ='upload'),
    url(r'signup',views.signup,name ='signup'),
    url(r'explore',views.index,name ='explore'),
    # path('signup/', signup_view, name="signup")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from insta.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile

from django.contrib.auth import views as instaViews 



urlpatterns = [
   	
    path('profile/edit', EditProfile, name='edit-profile'),
   	path('signup/', Signup, name='signup'),
   	path('login/', instaViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', instaViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   	path('changepassword/', PasswordChange, name='change_password'),
   	path('changepassword/done', PasswordChangeDone, name='change_password_done'),
   	path('passwordreset/', instaViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', instaViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', instaViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', instaViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
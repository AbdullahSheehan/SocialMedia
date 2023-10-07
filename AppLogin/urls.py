from django.urls import path
from AppLogin import views
app_name = 'AppLogin'
urlpatterns = [
    path('register/',views.signUp, name='register'),
    path('login/',views.loginUser, name='login'),
    path('ediiprofile/',views.profile, name='profile'),
    path('logout/',views.logoutUser, name='logout'),
    path('profile/', views.myprofile, name='myProfile'),
    path('user/<username>/', views.user, name='user'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
]
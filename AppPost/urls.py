from django.urls import path
from AppPost import views
app_name = 'AppPost'
urlpatterns = [
    path('',views.home, name='home'),
    path('like/<pk>/', views.liked, name='like'),
    path('unlike/<pk>', views.unliked, name='unlike'),
]
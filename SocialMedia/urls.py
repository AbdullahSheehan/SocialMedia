
from django.contrib import admin
from django.urls import path, include
from AppPost import views

urlpatterns = [
    path('', views.home , name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('AppLogin.urls')),
    path('post/', include('AppPost.urls')),
]

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
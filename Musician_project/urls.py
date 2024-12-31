
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('album/', include('album.urls')),
    path('musicians/',include('musician.urls')),
    path('user/',include('UserModel.urls')),
]

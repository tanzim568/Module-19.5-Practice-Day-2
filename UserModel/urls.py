from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('update/',views.UpdateProfile,name='update'),
    # path('login/',views.user_login,name='login')
    # path('logout/',views.user_logout,name='logout')
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('',views.HomeView.as_view(),name='profile'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('update/',views.UpdateProfileView.as_view(),name='update'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    # path('passwords/',views.pass_change,name='pass_change'),
    path('passwords/',views.UserPassChange.as_view(),name='pass_change'),
    path('passwords2/',views.pass_change2,name='pass_change2'),
    # path('logout/',LogoutView.as_view(next_page='homepage'),name='logout')
    
]
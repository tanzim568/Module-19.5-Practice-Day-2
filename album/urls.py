
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('add/',views.add_album,name='add_album'),
    # path('edit/<int:id>',views.edit,name='edit_album'),
    # path('delete/<int:id>',views.delete,name='delete_album'),
    path('add/',views.CreatViewAlbum.as_view(),name='add_album'),
    path('edit/<int:id>',views.EditView.as_view(),name='edit_album'),
    path('delete/<int:id>',views.DeleteViewAlbum.as_view(),name='delete_album'),
]

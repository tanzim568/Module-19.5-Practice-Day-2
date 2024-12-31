from django.shortcuts import render
from album.models import Album

# Create your views here.

def home(request):
    # albums=Album.objects.select_related('musician').all()
    albums=Album.objects.all()
    # for album in albums:
    #     print(album.musician.f_name)
    return render(request,'home.html',{'albums':albums})
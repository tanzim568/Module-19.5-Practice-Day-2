from django.shortcuts import render,redirect
from .import forms
from .models import Album
from .import models
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def add_album(request):
#     if request.method =="POST":
#         albumform=forms.AlbumForm(request.POST)
       
#         if albumform.is_valid():
#             albumform.save(commit=True)
#             return redirect('add_album')
        
    
#     else:
#         albumform=forms.AlbumForm()
#     return render(request,'add_album.html',{'form':albumform})


#add album as class view
class CreatViewAlbum(CreateView):
    model = models.Album
    form_class=forms.AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy('homepage')
    


# def edit(request,id):
#     data= Album.objects.get(pk=id)
#     albumform=forms.AlbumForm(instance=data)
    
#     # print(data)
#     if request.method =="POST":
#         albumform=forms.AlbumForm(request.POST,instance=data)
       
#         if albumform.is_valid():
#             albumform.save(commit=True)
#             return redirect('homepage')
        
    
#     # else:                  #as the edit request is on coming on post method so this block will execute so we need to terminate this block,otherwise albumform=forms.Albumform() will replace above albumform
#     #     albumform=forms.AlbumForm()
#     return render(request,'add_album.html',{'form':albumform})

class EditView(UpdateView):
    model=models.Album
    form_class=forms.AlbumForm
    template_name='add_album.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')
    
# def delete(request,id):
#     data=Album.objects.get(pk=id)
#     data.delete()
#     return redirect('homepage')

class DeleteViewAlbum(DeleteView):
    model=models.Album
    template_name='delete.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')
    
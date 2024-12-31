from django.shortcuts import render,redirect
from .import forms
from .models import Musician
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


# def add_musician(request):
#     if request.method == 'POST':
#         musiciain=forms.MusicianForm(request.POST)
#         if musiciain.is_valid():
#             musiciain.save(commit=True)
#             return redirect ('add_muscian')
        
#     else:
#         musiciain=forms.MusicianForm()
#     return render(request,'add_musician.html',{'form':musiciain})

#as class based view
class CreateMusician(CreateView):
    model= Musician
    form_class=forms.MusicianForm
    template_name='add_musician.html'
    success_url=reverse_lazy('homepage')
        
        
# def edit_musician(request,id):
#     data=Musician.objects.get(pk=id)
#     musiciain=forms.MusicianForm(instance=data)
#     if request.method == 'POST':
#         musiciain=forms.MusicianForm(request.POST ,instance=data)
#         if musiciain.is_valid():
#             musiciain.save(commit=True)
#             return redirect ('homepage')
        
#     # else:
#     #     musiciain=forms.MusicianForm()
#     return render(request,'add_musician.html',{'form':musiciain})
        
        
class EditMusician(UpdateView):
    model=Musician
    form_class=forms.MusicianForm
    template_name='add_musician.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')
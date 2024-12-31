from django.shortcuts import render,redirect
from .forms import RegistrationForm,ChangeUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.views.generic import FormView,CreateView,UpdateView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.views import View

# Create your views here.

# def home(request):
#     return render(request,'./user.html')

class HomeView(TemplateView):
    template_name = './user.html'

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Account Created Successfully')
#             return redirect('homepage')
#     else:
#         form=RegistrationForm()
#     return render(request,'./signup.html',{'form':form})

#class based view
class RegisterView(FormView):
    template_name='./signup.html'
    form_class=RegistrationForm
    success_url=reverse_lazy('profile')
    
    def form_valid(self,form):
        form.save()
        messages.success(self.request,'Account Created Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        form.save()
        messages.error(self.request,'Account Creation Failed.Try Again')
        return super().form_invalid(form)
    

# def UpdateProfile(request):
#     if request.method == 'POST':
#         form = ChangeUserForm(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Profile Updated')
#             return redirect('profile')
#     else:
#         form=ChangeUserForm(instance=request.user)
#     return render(request,'./update.html',{'form':form})

class UpdateProfileView(UpdateView):
    model=User
    template_name='update.html'
    form_class=ChangeUserForm
    success_url=reverse_lazy('profile')
    
    def form_valid(self,form):
        form.save()
        messages.success(self.request,'Your Profile has been updated')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        form.save()
        messages.error(self.request,'Please try again later')
        return super().form_invalid(form)
    
    def get_object(self,queryset=None):
        return self.request.user
    
    
# def user_login(request):
#     if request.method == 'POST':
#         form=AuthenticationForm(request=request,data=request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['username']
#             user_pass=form.cleaned_data['password']
#             user=authenticate(username=name,password=user_pass)
#             if user is not None:
#                 login(request,user)
#                 return redirect('profile')
#             else:
#                 messages.error(request,'Login information Incorrect')
#                 return redirect('login')
#     else:
#         form=AuthenticationForm()
        
#     return render(request,'./login.html',{'form':form}) 

#class based login
class UserLoginView(LoginView):
    template_name='./login.html'
    success_url=reverse_lazy('profile')
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    
    def form_valid(self,form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Login information incorrect')
        return super().form_invalid(form)
    
def user_logout(request):
    logout(request)
    return redirect('homepage')

# class UserLogoutView(LogoutView):
#     success_url=reverse_lazy('homepage')
    
class UserLogoutView(View):
    # next_page = reverse_lazy('homepage')
    def get(self,request):
        logout(request)
        return redirect('homepage')

# def pass_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Password Updated Successfully')
#             update_session_auth_hash(request,form.user)
#             return redirect('profile')
        
            
#     else:
#         form=PasswordChangeForm(user=request.user)
#     return render(request,'./pass_change.html',{'form':form})

class UserPassChange(PasswordChangeView):
    template_name='./pass_change.html'
    success_url=reverse_lazy('profile')
    
    def form_valid(self,form):
        response=super().form_valid(form)
        messages.success(self.request,'Password Updated Successfully')
        return response
            
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
            
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'./pass_change.html',{'form':form})
            
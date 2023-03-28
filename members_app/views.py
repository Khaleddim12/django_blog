from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

from .forms import *

# Create your views here.

class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'members_app/forms/register.html'
    success_url = reverse_lazy('members_app:login')
    
class UpdateProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'members_app/forms/edit_profile.html'
    success_url = reverse_lazy('blog_app:PostListView')
    
    def get_object(self):
        return self.request.user
    
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChaningForm
    template_name = 'members_app/forms/change_password.html'
    success_url = reverse_lazy('blog_app:PostListView')
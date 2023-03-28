from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'members_app'

urlpatterns = [
    path('UserRegisterView/', views.UserRegisterView.as_view(), name='UserRegisterView'),
    path('login/', auth_views.LoginView.as_view(template_name='members_app/forms/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('updateProfile/', views.UpdateProfileView.as_view(), name = 'UpdateProfileView'),
    path('password/', views.PasswordChangeView.as_view(), name = 'PasswordChangeView'),
]
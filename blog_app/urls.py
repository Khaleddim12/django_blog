from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostListView'),
    path('post/<int:pk>', views.postDetailView.as_view(), name='PostDetailView'),
    path('add_post/',login_required(views.PostCreateView.as_view()), name='PostCreateView'),
    path('post/edit/<int:pk>', login_required(views.PostUpdateView.as_view(), login_url= reverse_lazy('members_app:login')), name='PostUpdateView'),
    path('post/<int:pk>/delete', login_required(views.PostDeleteView.as_view(), login_url= reverse_lazy('members_app:login')), name = 'PostDeleteView'),
    path('like/<int:pk>', views.like, name = 'like'),
    
    #category
    path('category', login_required(views.CategoryCreateView.as_view()), name = 'CategoryCreateView'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name = 'CategoryDetailView'),
    path('category/categories', views.CategoryListView.as_view(), name = 'CategoryListView'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name = 'CategoryDeleteView'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name = 'CategoryUpdateView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
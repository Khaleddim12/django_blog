from django.shortcuts import render,get_object_or_404
from .models import *

from .forms import *
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.http import HttpResponseRedirect
# Create your views here.



class PostListView(ListView):
    model = Post
    template_name = "blog_app/index.html"
    cats = Category.objects.all()
    ordering = ['-post_date']
    
def like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('blog_app:PostDetailView', args=[str(pk)]))

    

class postDetailView(DetailView):
    model = Post
    template_name = "blog_app/article_details.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
    


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog_app/forms/add_post_form.html"


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog_app/forms/edit_post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/confirmDeletion/post_confirm_delete.html'
    def get_success_url(self):
        return reverse('blog_app:PostListView')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/forms/add_category_form.html"
    

class CategoryListView(ListView):
    model = Category
    template_name = "blog_app/categories.html"
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog_app/category_details.html"


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'blog_app/confirmDeletion/category_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('blog_app:CategoryListView')
    

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/forms/edit_post_form.html"

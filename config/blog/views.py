from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BlogForm
from django.urls import reverse_lazy

from .models import Blog

#function based view
def blogs(request):
    context = {
        'blogs': Blog.objects.all()  # Blog.objects.all() is a QuerySet object (list of objects) from the Blog model (Blog.objects.all() is a list of Blog objects)
    }
    return render(request, 'blogs/blogs.html', context)

def blog_detail(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_detail.html', context)

def blog_details(request, blog_id):
    context = {
        'blog': Blog.objects.get(id=blog_id)
    }
    return render(request, 'blogs/blog_details.html', context) 

class BlogCreateView(CreateView): # new
    model = Blog
    #form_class = BlogForm
    template_name = 'blogs/blog_create.html'
    fields = ['title','subtitle', 'body','header_image']   #or fields = '__all__'
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    # 
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # new
    model = Blog
    # form_class = BlogForm
    template_name = 'blogs/blog_edit.html'
    fields = ['title','subtitle', 'body','header_image']  
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user  

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): # new
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('my_blogs') 

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

def my_blogs(request):
    current_user = request.user
    currentuser_blogs = Blog.objects.filter(author=current_user)
    context = {
        'blogs': currentuser_blogs
    }
    return render(request, 'blogs/my_blog.html', context)

# Create your views here.

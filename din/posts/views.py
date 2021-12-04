from django.http import request
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .models import Post
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



# def home(request):
#     context ={
#         'posts': Post.objects.all()
#     }
#     return render(request, 'posts/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-datetime']

class PostDetailView(DetailView):
    model = Post 


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'description']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
          


class PostUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    fields = ['title', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



    

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post 
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False





    

def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})
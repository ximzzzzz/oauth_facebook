from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,CreateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostList(ListView):
    model = Post
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title','content')
    success_url = reverse_lazy('posts:list')
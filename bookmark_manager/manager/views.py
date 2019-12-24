from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post

class ManagerListView(ListView):
    model = Post
    template_name = 'home.html'

class ManagerDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
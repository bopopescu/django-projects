from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Post

class ManagerListView(ListView):
    model = Post
    template_name = 'home.html'

class ManagerDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ManagerCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class ManagerUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['url','body']

class ManagerDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

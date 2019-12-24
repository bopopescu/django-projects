from django.urls import path
from .views import ManagerListView,ManagerDetailView,ManagerCreateView,ManagerUpdateView


urlpatterns = [
    path('post/<int:pk>/', ManagerDetailView.as_view(), name='post_detail'),
    path('', ManagerListView.as_view(), name='home'),
    path('post/new/', ManagerCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',
ManagerUpdateView.as_view(), name='post_edit'), # new
]
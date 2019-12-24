from django.urls import path
from .views import ManagerListView,ManagerDetailView


urlpatterns = [
    path('post/<int:pk>/', ManagerDetailView.as_view(), name='post_detail'),
    path('', ManagerListView.as_view(), name='home'),
]
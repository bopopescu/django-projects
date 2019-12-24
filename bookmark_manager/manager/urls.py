from django.urls import path
from .views import ManagerListView


urlpatterns = [
    path('', ManagerListView.as_view(), name='home'),
]
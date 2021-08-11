from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /app
    path('dashboard', views.dashboard, name='dashboard')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /app
    path('data', views.data, name='data'),
    path('dashboard', views.dashboard, name='dashboard')
]

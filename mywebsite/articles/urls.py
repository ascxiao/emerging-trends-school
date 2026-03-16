from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles_index'),
    path('add/', views.add, name='articles_add'),
]

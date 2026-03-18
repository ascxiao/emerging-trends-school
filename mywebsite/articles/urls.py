from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles_index'),
    path('add/', views.add, name='articles_add'),
    path('delete/', views.delete, name='articles_delete'),
    path('<int:article_id>/', views.detail, name='articles_detail'),
    path('<int:article_id>/delete/', views.delete, name='articles_delete'),
    path('<int:article_id>/edit/', views.edit, name='articles_edit'),
]

from .import views

from django.urls import path

urlpatterns = [
    path('blog/', views.index, name='blog-index'),  # root url, means the first page
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),

]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # http:127.0.0.1:8000/post/<pkの値>/で表示
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]

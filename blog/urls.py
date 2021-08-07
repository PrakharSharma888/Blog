from django.contrib import admin
from django.urls import path
from .views import PostListViews, PostDetailViews, PostCreateViews, PostUpdateViews, PostDeleteView, UserPostListViews
from . import views

urlpatterns = [
    path('', PostListViews.as_view(), name='postt'),
    path('search', views.search, name='search'),
    path('about',views.about, name='about'),
    path('user/<username>', UserPostListViews.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailViews.as_view(), name='post-details'),
    path('post/new', PostCreateViews.as_view(), name='post-new'),
    path('post/<int:pk>/update', PostUpdateViews.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),  # Requiers a form for confirmation
]

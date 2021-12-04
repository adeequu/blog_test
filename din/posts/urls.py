from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='posts=home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
    path('post/new/', PostCreateView.as_view(), name='posts-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
    path('about/', views.about, name='posts-about'),

]
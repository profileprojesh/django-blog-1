from django.urls import path
from . import views

urlpatterns=[
    path('', views.PostListView.as_view(), name='home'),
    path('postcreate/',views.PostCreateView.as_view(), name='create-post'),
    path('search/',views.SearchView, name='search-post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='each-post'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
]
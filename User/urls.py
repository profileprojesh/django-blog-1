from django.urls import path
from . import views

urlpatterns=[
    path('newuser/',views.CreateUserView.as_view(), name='create_user'),
    path('profile/',views.UpdateUserView, name='update_user'),

]
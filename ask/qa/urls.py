from django.urls import path, re_path
from qa import views

urlpatterns = [
    path ('', views.test, name='test'),
    path ('login/', views.test, name='login'),
    path ('signup/', views.test, name='singup'),
    re_path (r'^question/\d+/', views.test, name='question'),
    path ('ask/', views.test, name='ask'),
    path ('popular/', views.test, name='popular'),
    path ('new/', views.test, name='new'),
]
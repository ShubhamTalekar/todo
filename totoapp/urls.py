from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='registration-page'),
    path('login/', views.loginpage, name='login-page'),
    path('logout/', views.logoutview, name='logout'),
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
]


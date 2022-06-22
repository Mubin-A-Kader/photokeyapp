from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.gallery, name='gallery'),
    #path('photo/<str:pk>/', views.viewphotoafterVerified, name='photo'),
    path('photos/<str:pk>/', views.zlewPhoto, name='photos'),
    path('add/', views.addPhoto, name='add'),
    path('addvideo/', views.addVideo, name='addVideo'),
   path('keyverify', views.keyVerify, name='keyverify'),
   path('keyhtml', views.keyhtml, name='keyhtml'),
   path('photo', views.zlewPhoto, name='photo'),
   
   
]
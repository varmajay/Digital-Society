from django.urls import path
from .import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password',views.forgot_password,name='forgot-password'),
    path('add-house',views.add_house,name='add-house'),
    path('view-house',views.view_house,name='view-house'),

]
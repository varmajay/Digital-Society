from .import views
from django.urls import path

urlpatterns = [
    path('',views.member_index,name='member-index'),
    path('member-login',views.member_login,name='member-login'),
    path('member-logout',views.member_logout,name='member-logout'),
    path('member-profile',views.member_profile,name='member-profile')
]
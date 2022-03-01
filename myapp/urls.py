from django.urls import path
from .import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('add-house/',views.add_house,name='add-house'),
    path('view-house/',views.view_house,name='view-house'),
    path('house-edit/<int:pk>',views.house_edit,name='house-edit'),
    path('house-delete/<int:pk>',views.house_delete,name='house-delete'),
    path('create-member/',views.create_member,name='create-member'),
    path('view-member/',views.view_member,name='view-member'),
    path('edit-member/<int:pk>',views.edit_member,name='edit-member'),
    path('delete-member/<int:pk>',views.delete_member,name='delete-member'),
    path('contact/',views.contact,name='contact'),
    path('contact-view/',views.contact_view,name='contact-view'),
    path('contact-edit/<int:pk>',views.contact_edit,name='contact-edit'),
    path('contact-delete/<int:pk>',views.contact_delete,name='contact-delete'),
    path('event-gallery/',views.event_gallery,name='event-gallery'),
    path('event-gallery-view/',views.event_gallery_view,name='event-gallery-view'),

]
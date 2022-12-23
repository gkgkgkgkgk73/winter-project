from django.urls import path
from . import views

urlpatterns = [
    path('trait/', views.get_trait_info, name='trait/'),
    path('item/', views.get_item_info, name='item/'),
    path('augment/', views.get_augment_info, name='augment/'),
    path('champion/', views.get_champion_info, name='champion/'),
    path('trait/<int:trait_id>/', views.get_trait_detail, name='outfit/get_trait_detail/'),
]
from django.urls import path
from . import views

urlpatterns = [
    # Leave as an empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('physical_products/', views.physical, name="physical"),
    path('digital_products/', views.nonPhysical, name="non-physical"),
    path('sports/', views.sports, name="sports"),
    path('DVDs/', views.DVDs, name="DVDs"),
    path('toys/', views.toys, name="toys"),
    path('video_games/', views.videoGames, name="video_games"),
    path('youtuber_needs/', views.youtuberNeeds, name="youtuber_needs"),
    path('clothes/', views.clothes, name="clothes"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('reserve/', views.reserve),
    path('gallery/', views.gallery),
    path('signup/', views.signup),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('orders/', views.order_history, name='order_history'),
    path('increase/<int:item_id>/', views.increase_qty, name='increase_qty'),
    path('decrease/<int:item_id>/', views.decrease_qty, name='decrease_qty'),


]

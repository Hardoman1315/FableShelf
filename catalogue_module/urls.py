from django.urls import path
from . import views


app_name = "catalogue_module"

urlpatterns = [
    path('', views.redirect_to_index, name='redirect_to_index'),
    path('categories/<int:category_id>/', views.catalogue_page, name='catalogue'),
    path('book/<int:book_id>/', views.book_page, name="book_page"),
    path('book/add_to_cart/<int:book_id>/', views.add_to_cart, name="add_to_cart"),
    path('book/<int:book_id>/add_review/', views.add_review, name="add_review"),
    path('author/', views.authors_page, name='authors_page'),
    path('author/<int:author_id>/', views.author_page, name="author_page"),
    path('discounts/', views.discounts_page, name='discounts_page'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart_page, name='cart_page'),
    path('cart/remove/<int:cart_id>/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/remove/all/', views.clear_cart, name='clear_cart'),
    path('cart/confirm/<int:cart_id>/', views.confirm_payment, name='confirm_payment'),
    path('cart/confirm/all/', views.confirm_all_payments, name='confirm_all'),
]

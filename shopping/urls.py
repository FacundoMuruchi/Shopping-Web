from django.urls import path
from .views import about_view, cart_view, PostListView

urlpatterns=[
    path('about/', about_view, name='about'),
    path('shop/', PostListView.as_view(), name='shop'),
    path('cart/', cart_view, name='cart')
]
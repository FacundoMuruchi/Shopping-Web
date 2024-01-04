from django.urls import path
from .views import about_view, cart_view, PostListView, PostDetailView

urlpatterns=[
    path('about/', about_view, name='about'),
    path('shop/', PostListView.as_view(), name='shop'),
    path('cart/', cart_view, name='cart'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='details')
]
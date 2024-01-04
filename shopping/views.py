from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

def about_view(request):
    return render(request=request, template_name='shopping/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'shopping/shop.html'

def cart_view(request):
    return render(request=request, template_name='shopping/cart.html')
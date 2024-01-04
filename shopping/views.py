from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

def about_view(request):
    return render(request=request, template_name='shopping/about.html')

def cart_view(request):
    return render(request=request, template_name='shopping/cart.html')

class PostListView(ListView):
    model = Post
    template_name = 'shopping/shop.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'shopping/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega los productos relacionados a la variable 'object_list'
        context['object_list'] = Post.objects.exclude(pk=self.object.pk)[:4]
        return context
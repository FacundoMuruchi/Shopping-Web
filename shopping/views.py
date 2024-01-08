from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


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
    
class PostCreateView(LoginRequiredMixin,CreateView):
        model = Post
        fields = ['title', 'desc', 'img', 'price']
        template_name = 'shopping/upload.html'
        success_url = reverse_lazy('shop')

        def form_valid(self, form):
            """If the form is valid, save the associated model."""
            form.instance.creator = self.request.user
            return super().form_valid(form)
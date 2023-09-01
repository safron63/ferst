from django.views.generic import ListView
from django.shortcuts import render

from market.models import Product

class ProductListView(ListView):
    model=Product
    template_name='market/index.html'
    context_object_name='products'

def post_list(request):
    return render(request, 'blog/post_list.html', {})
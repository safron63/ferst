from django.views.generic import ListView

from market.models import Product

class ProductListView(ListView):
    model=Product
    template_name='market/index.html'
    context_object_name='products'
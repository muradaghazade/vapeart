from django.views.generic import TemplateView, ListView , DetailView , CreateView
from .forms import CreateOrderForm
from .models import FAQ, AboutUS, Brand, Order, Product, Slider, Category, Brand, Shipping
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by("-id")
        context['sliders'] = Slider.objects.order_by("-id")
        context['categories'] = Category.objects.order_by("-id")
        context['brands'] = Brand.objects.order_by("-id")
        return context


class ProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'
    # paginate_by = 8
    queryset = Product.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by("-id")
        context['brands'] = Brand.objects.order_by("-id")
        return context

    def get_queryset(self):
        queryset = Product.objects.order_by("-id")
        category = self.request.GET.get('category')
        title = self.request.GET.get('title')
        if category:
            queryset = queryset.filter(category__title=category)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.filter(category=self.object.category)
        context['brands'] = Brand.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = AboutUS.objects.order_by("-id").first()
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.order_by("-id")
        return context


class BrandsView(ListView):
    model = Brand
    context_object_name = 'brands'
    template_name = 'brands.html'
    queryset = Brand.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.order_by("-id")
        return context


class ShippingView(TemplateView):
    template_name = 'shipping.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = Shipping.objects.order_by("-id").first()
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.order_by("-id")
        return context


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.order_by("-id")
        return context


class FAQView(ListView):
    model = FAQ
    context_object_name = 'faqs'
    template_name = 'faq.html'
    queryset = FAQ.objects.order_by("-id")


class OrderView(CreateView):
    model = Order
    template_name = 'cart.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by("-id")
        context['products'] = Product.objects.order_by("-id")
        return context


# def add_to_cart(request):
#     if request.method == 'GET':

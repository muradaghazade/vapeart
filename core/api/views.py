from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from core.models import Product
from .serializers import ProductSerializer


class ProductsAPIView(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by('-id')

    def get_queryset(self):
        queryset = Product.objects.none()
        ids = self.request.data.get('ids')
        for id in ids:
            queryset |= Product.objects.filter(pk=id)

        # if id:
        #     queryset = queryset.filter(title=id)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
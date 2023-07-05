from rest_framework import viewsets, permissions
from consumer.models import Product, Order
from consumer.serializers import ProductSerializer, OrderSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]



class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to create, view or edit order.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

    def get_queryset(self):
        session = self.request.session
        return Order.objects.filter(session = session)
    
    
    def create(self, request):
        pass
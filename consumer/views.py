from rest_framework import viewsets, permissions
from consumer.models import Product
from consumer.serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
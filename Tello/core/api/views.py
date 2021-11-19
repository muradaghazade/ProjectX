from rest_framework.generics import CreateAPIView
from core.models import ProductVersion
from .serializers import ProductVersionSerializer

class ProductVersionAPIView(CreateAPIView):
    model = ProductVersion
    serializer_class = ProductVersionSerializer
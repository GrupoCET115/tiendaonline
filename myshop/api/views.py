from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Product
from api.serializers import ProductSerializer, FeedbackShopSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST'])
def feedbackshop_list(request):
    if request.method == 'POST':
        serializer = FeedbackShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
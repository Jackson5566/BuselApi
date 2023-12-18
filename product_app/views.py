from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from product_app.models import ProductModel
from .serializers import EditProductSerializer, ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from utilites.get_products import get_products
from utilites.add_security import access_protected
from django_filters.rest_framework import DjangoFilterBackend
from product_app.classes.search import SearchAlgorithm


@access_protected
class ProductView(APIView):
    def post(self, request):
        product_serializer = EditProductSerializer(data=request.data, context={
            'request': request
        })

        if product_serializer.is_valid(raise_exception=True):
            new_product = product_serializer.create(product_serializer.validated_data)
            new_product_serializer = ProductSerializer(instance=new_product)

            return Response(new_product_serializer.data, status=status.HTTP_200_OK)

    def get(self, request, id):
        instance = get_object_or_404(ProductModel, id=id)
        product_serializer = ProductSerializer(instance=instance)

        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        product_serializer = EditProductSerializer(data=request.data)

        if product_serializer.is_valid(raise_exception=True):
            product_instance = get_object_or_404(ProductModel, id=id)
            product_serializer.update(instance=product_instance, **product_serializer.validated_data)

            return Response({
                'message': '¡Creado con éxito!'
            }, status=status.HTTP_200_OK)

    def delete(self, request, id):
        instance = get_object_or_404(ProductModel, id=id)
        instance.delete()

        return Response({
            'message': '¡Eliminado con éxito!'
        }, status=status.HTTP_200_OK)


@get_products
class ProductsView(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']

    def get_queryset(self):
        return ProductModel.objects.all()


@get_products
class SearchProductsView(ListAPIView):
    def get_queryset(self):
        search = SearchAlgorithm(request=self.request)
        search.start_process()
        return search.queryset

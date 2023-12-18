from os import path
from rest_framework.serializers import ModelSerializer
from product_app.models import ProductModel


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductModel

    def to_representation(self, instance):
        rel = super().to_representation(instance=instance)
        rel['image'] = path.basename(instance.image.name)
        return rel


class EditProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('name', 'description', 'image', 'price', 'quantity')

    def create(self, validated_data):
        instance = ProductModel.objects.create(**validated_data, user=self.context['request'].user)
        return instance

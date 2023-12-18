from product_app.paginations import ProductPagination
from product_app.serializers import ProductSerializer


def get_products(cls):
    setattr(cls, 'serializer_class', ProductSerializer)
    setattr(cls, 'pagination_class', ProductPagination)
    return cls
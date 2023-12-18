from django.db.models.signals import pre_delete
from django.dispatch import receiver
from product_app.models import ProductModel
from firebase_admin import storage as firebase_storage


@receiver(pre_delete, sender=ProductModel)
def product_callback(sender, instance, *args, **kwargs):
    try:
        file = firebase_storage.bucket().blob(instance.image.name)
        file.delete()
    except:
        pass

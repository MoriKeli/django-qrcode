from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Products
import uuid


@receiver(pre_save, sender=Products)
def generate_productID(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:12]

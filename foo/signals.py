from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from .gql import updateBar


@receiver(post_save, sender='foo.Bar')
def seat_post_save(sender, instance, created, **kwargs):
    async_to_sync(updateBar)(instance)

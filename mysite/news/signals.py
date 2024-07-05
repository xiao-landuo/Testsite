from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import News


@receiver(post_save, sender=News, weak=False)
def create_news(sender, instance, created, **kwargs):
    if created:
        print("* " * 50)
        print(f"Добавлена новая новость - {instance.title}")
        print("* " * 50)


# @receiver(post_delete, sender=News)
# def create_profile(sender, instance, **kwargs):
#     print("* " * 50)
#     print(f"Удалена категория - {instance.title}")
#     print("* " * 50)

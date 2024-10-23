from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from .models import News, Subscriber

@receiver(m2m_changed, sender=News.categories.through)
def send_notifications_on_post_publish(sender, instance, action, **kwargs):
    if action == 'post_add':
        categories = instance.categories.all()
        subscribers = Subscriber.objects.filter(category__in=categories).select_related('user')

        for subscriber in subscribers:
            send_mail(
                subject=f'Новая статья в категории {subscriber.category.name}',
                message=f'Прочитайте статью "{instance.title}" по ссылке {reverse("news_detail", args=[instance.id])}',
                from_email='admin@newsportal.com',
                recipient_list=[subscriber.user.email],
            )

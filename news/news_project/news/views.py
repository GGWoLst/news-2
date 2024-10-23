from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Subscriber, News

def send_weekly_newsletter():
    subscribers = Subscriber.objects.all()
    last_week = now() - timedelta(days=7)
    news_last_week = News.objects.filter(published_at__gte=last_week)

    for subscriber in subscribers:
        user_news = news_last_week.filter(categories=subscriber.category)
        if user_news.exists():
            message = 'Список новостей за последнюю неделю:\n'
            for news_item in user_news:
                message += f'- {news_item.title} ({reverse("news_detail", args=[news_item.id])})\n'
            send_mail(
                subject='Еженедельная рассылка новостей',
                message=message,
                from_email='admin@newsportal.com',
                recipient_list=[subscriber.user.email],
            )

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

scheduler.add_job(
    send_weekly_newsletter,
    trigger='cron',
    day_of_week='fri',
    hour=18,
    minute=0,
    id='weekly_newsletter',
    max_instances=1,
    replace_existing=True,
)

scheduler.start()

from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_list = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})

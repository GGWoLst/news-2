from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import News

class NewsFilter(FilterSet):
    date_after = DateTimeFilter(
        field_name='date_published',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = News
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }

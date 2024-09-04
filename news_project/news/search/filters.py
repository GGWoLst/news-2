import django_filters
from django_filters import DateTimeFilter
from .models import News

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    added_after = DateTimeFilter(field_name='added_at', lookup_expr='gte', widget=django_filters.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = News
        fields = ['title', 'category', 'added_after']

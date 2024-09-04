from django.contrib.auth.models import Group, Permission
from django.apps import apps

authors_group, created = Group.objects.get_or_create(name='authors')

content_types = [
    apps.get_model('news', 'Article'),  
    apps.get_model('news', 'News'),   
]

for content_type in content_types:
    permissions = Permission.objects.filter(content_type=content_type)
    authors_group.permissions.add(*permissions)
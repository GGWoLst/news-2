from django.db import models

class Post(models.Model):
    TITLE_CHOICES = [
        ('news', 'News'),
        ('article', 'Article'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=7, choices=TITLE_CHOICES)
    category = models.CharField(max_length=50, default='General')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

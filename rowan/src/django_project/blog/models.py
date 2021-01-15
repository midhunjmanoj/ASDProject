from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

BLOG_CHOICES=[
        ("General","General"),
        ("Food","Food"),
        ("Travel","Travel"),
        ("Technology","Technology"),
        ("Fashion","Fashion"),
        ("Movies","Movies"),
        ("Politics","Politics"),
        ("Gaming","Gaming"),
        ("Business","Business"),
        ("Sports","Sports"),
        ]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=BLOG_CHOICES, default="General")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField('Заголовок', max_length=500)
    date = models.DateTimeField('Дата публикации',)
    body = models.TextField()
    deleted = models.BooleanField()

    def __str__(self):
        return self.body[:15]


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField('Заголовок', max_length=500)
    date = models.DateTimeField('Дата комментария', auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.title[:15]
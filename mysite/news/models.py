from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, max_length=1000, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Likes(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Пост')
    likes = models.IntegerField(default=0, verbose_name='Всего лайков')

    def __str__(self):
        return f'{self.post}:{self.likes}'

    class Meta:
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Пост')
    commentator_name = models.CharField(max_length=50, verbose_name='Имя комментатора', default="None")
    comment = models.TextField(max_length=1000, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.post}:{self.comment[:50]}'

    def in_post(self, post):
        if self.post == post:
            return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

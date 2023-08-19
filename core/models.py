from django.contrib.auth.models import User
from django.db import models


class DictRefType(models.Model):
    TYPE = (
        (1, 'website'),
        (2, 'book'),
        (3, 'article'),
        (4, 'music'),
        (5, 'video'),
    )
    type = models.IntegerField("Тип ссылки", choices=TYPE, primary_key=True)

    def __str__(self):
        return self.get_type_display()


class Bookmark(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок сайта', max_length=100)
    description = models.CharField('Краткое описание', max_length=200, blank=True, null=True)
    ref = models.CharField('Ссылка на страницу', max_length=200)
    type = models.ForeignKey(DictRefType, on_delete=models.CASCADE)
    image = models.CharField('Картинка превью', max_length=150, blank=True, null=True)
    date_created = models.DateTimeField('Время создания', auto_now_add=True)
    date_edit = models.DateTimeField('Время последнего изменения', auto_now=True)


class Collection(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название коллекции', max_length=100)
    description = models.CharField('Краткое описание', max_length=150, blank=True, null=True)
    date_created = models.DateTimeField('Время создания', auto_now_add=True)
    date_edit = models.DateTimeField('Время последнего изменения', auto_now=True)
    bookmarks = models.ManyToManyField(Bookmark)

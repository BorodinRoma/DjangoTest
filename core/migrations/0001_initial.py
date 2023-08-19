# Generated by Django 4.2.3 on 2023-08-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок сайта')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('ref', models.CharField(max_length=150, verbose_name='Ссылка на страницу')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка превью')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
            ],
        ),
        migrations.CreateModel(
            name='DictRefType',
            fields=[
                ('type', models.IntegerField(choices=[(1, 'website'), (2, 'book'), (3, 'article'), (4, 'music'), (5, 'video')], primary_key=True, serialize=False, verbose_name='Тип ссылки')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название коллекции')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Краткое описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('bookmarks', models.ManyToManyField(to='core.bookmark')),
            ],
        ),
    ]

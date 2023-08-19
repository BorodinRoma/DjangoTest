# Generated by Django 4.2.3 on 2023-08-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bookmark_created_by_collection_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dictreftype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='image',
            field=models.CharField(blank=True, null=True, verbose_name='Картинка превью'),
        ),
    ]

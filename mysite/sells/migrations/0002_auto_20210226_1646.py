# Generated by Django 3.1.7 on 2021-02-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sells',
            options={'verbose_name': 'Продажа', 'verbose_name_plural': 'Продажи'},
        ),
        migrations.AlterField(
            model_name='sells',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='sells',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]

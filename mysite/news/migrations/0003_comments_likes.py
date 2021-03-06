# Generated by Django 3.1.7 on 2021-02-27 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210226_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0, verbose_name='Всего лайков')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Лайки',
                'verbose_name_plural': 'Лайки',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000, verbose_name='Комментарий')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]

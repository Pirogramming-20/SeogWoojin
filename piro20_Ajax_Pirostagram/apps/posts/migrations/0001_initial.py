# Generated by Django 5.0.1 on 2024-01-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='수정일')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('image', models.ImageField(blank=True, upload_to='ideas/%Y%m%d', verbose_name='이미지')),
                ('content', models.CharField(max_length=100, verbose_name='내용')),
            ],
        ),
    ]

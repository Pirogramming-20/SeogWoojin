# Generated by Django 5.0.1 on 2024-01-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('release_date', models.IntegerField()),
                ('director', models.CharField(max_length=32)),
                ('actor', models.TextField()),
                ('genre', models.CharField(max_length=32)),
                ('stars', models.DecimalField(decimal_places=1, max_digits=3)),
                ('running_time', models.IntegerField()),
                ('review', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
    ]
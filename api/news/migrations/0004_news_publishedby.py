# Generated by Django 5.0.1 on 2024-01-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publishedBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

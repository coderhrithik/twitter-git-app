# Generated by Django 4.2.3 on 2023-11-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0008_alter_tweet_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

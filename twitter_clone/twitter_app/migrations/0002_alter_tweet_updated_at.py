# Generated by Django 4.2.3 on 2023-10-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

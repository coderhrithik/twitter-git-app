# Generated by Django 4.2.3 on 2023-10-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0004_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
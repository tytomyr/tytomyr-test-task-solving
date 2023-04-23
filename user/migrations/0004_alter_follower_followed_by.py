# Generated by Django 4.0.2 on 2023-04-23 21:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_follower_followed_by_follower_followed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='followed_by',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.2 on 2022-02-12 12:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_comment_approved'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostLike',
            new_name='Like',
        ),
    ]
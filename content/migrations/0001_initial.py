# Generated by Django 3.2 on 2022-03-01 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vimeo_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=1)),
                ('related_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related', to='content.video')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Video_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Video_categories',
            },
        ),
        migrations.CreateModel(
            name='VideoView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.video')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='content.video_category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default='')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.video')),
            ],
        ),
    ]

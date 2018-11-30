# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 14:55
from __future__ import unicode_literals

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
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_public', models.BooleanField(default=True, verbose_name='public')),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='marcador.Tag'),
        ),
    ]

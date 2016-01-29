# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 08:14
from __future__ import unicode_literals

import SenseWeb.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', SenseWeb.models.TinyTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', SenseWeb.models.TinyTextField()),
                ('description', models.TextField()),
                ('imdb_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('link', models.URLField()),
                ('trailer', models.URLField()),
                ('genres', models.CommaSeparatedIntegerField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_type', SenseWeb.models.TinyTextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField()),
                ('content', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SenseWeb.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='follow_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_quiz', to='SenseWeb.Quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SenseWeb.Quiz'),
        ),
    ]

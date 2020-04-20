# Generated by Django 2.2.12 on 2020-04-12 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=250)),
                ('event_start', models.DateTimeField()),
                ('participants', models.TextField()),
                ('event_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('username', models.CharField(max_length=250)),
                ('email_address', models.CharField(max_length=250)),
                ('last_participation', models.DateTimeField()),
            ],
        ),
    ]
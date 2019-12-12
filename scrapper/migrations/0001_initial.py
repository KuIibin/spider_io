# Generated by Django 2.2.7 on 2019-12-12 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=250)),
                ('scrapping_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

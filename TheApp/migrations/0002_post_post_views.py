# Generated by Django 2.2.5 on 2020-01-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_views',
            field=models.IntegerField(default=0),
        ),
    ]

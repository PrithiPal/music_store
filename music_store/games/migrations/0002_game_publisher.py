# Generated by Django 3.0.5 on 2020-04-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

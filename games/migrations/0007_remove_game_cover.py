# Generated by Django 3.0.5 on 2020-04-21 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='cover',
        ),
    ]

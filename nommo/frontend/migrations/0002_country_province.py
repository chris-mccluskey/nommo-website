# Generated by Django 2.2.2 on 2019-06-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='province',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_country_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
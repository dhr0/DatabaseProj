# Generated by Django 2.0 on 2017-12-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0005_auto_20171211_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='avgrate',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 2.0 on 2017-12-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0002_auto_20171211_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='text',
            field=models.CharField(default='', max_length=500),
        ),
    ]

# Generated by Django 2.0 on 2017-12-11 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0004_feedbacks_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='BookStore.Books'),
        ),
    ]

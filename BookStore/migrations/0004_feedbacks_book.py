# Generated by Django 2.0 on 2017-12-11 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0003_feedbacks_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BookStore.Books'),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1.5 on 2019-01-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20190129_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
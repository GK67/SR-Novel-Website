# Generated by Django 2.1.5 on 2019-01-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20190129_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='content',
            field=models.TextField(default='Enter content of the chapter'),
        ),
    ]
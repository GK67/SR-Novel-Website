# Generated by Django 2.1.5 on 2019-01-30 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_merge_20190129_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_image',
            new_name='bookImage',
        ),
    ]

# Generated by Django 2.1 on 2021-01-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Food', 'Food'), ('Travel', 'Travel'), ('Technology', 'Technology'), ('Fashion', 'Fashion'), ('Movies', 'Movies'), ('Politics', 'Politics'), ('Gaming', 'Gaming'), ('Business', 'Business'), ('Sports', 'Sports')], default='Personal', max_length=20),
        ),
    ]

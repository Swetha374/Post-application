# Generated by Django 4.0.6 on 2022-08-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to='postimages'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='dislike_count',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, help_text='블로그 이미지', null=True, upload_to=''),
        ),
    ]

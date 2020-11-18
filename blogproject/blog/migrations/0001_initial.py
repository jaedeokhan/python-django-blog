# Generated by Django 3.1.2 on 2020-11-18 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='블로그 제목', max_length=200)),
                ('category', models.CharField(help_text='블로그 카테고리', max_length=30)),
                ('content', models.TextField(help_text='블로그 내용')),
                ('view_count', models.IntegerField(default=0, help_text='블로그 조회수')),
                ('like_count', models.IntegerField(default=0, help_text='블로그 추천수')),
                ('dislike_count', models.IntegerField(default=0, help_text='블로그 비추천수')),
                ('create_date', models.DateField(auto_now_add=True, help_text='블로그 게시물 생성일')),
                ('update_date', models.DateField(auto_now=True, help_text='블로그 게시물 수정일')),
                ('user', models.ForeignKey(blank=True, help_text='블로그 사용자', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

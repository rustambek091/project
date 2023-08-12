# Generated by Django 4.2.1 on 2023-07-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_servicess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('blog_mavzusi', models.CharField(max_length=30)),
                ('post_haqida', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('img', models.ImageField(upload_to='images')),
                ('user_comment', models.CharField(max_length=125)),
                ('time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('loyiha_haqida', models.CharField(max_length=255)),
                ('prospotr', models.CharField(max_length=5)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='abouts',
        ),
        migrations.DeleteModel(
            name='servicess',
        ),
    ]

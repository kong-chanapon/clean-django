# Generated by Django 5.0.7 on 2024-08-26 14:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('file_name', models.CharField(max_length=255)),
                ('file_extension', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'BlogImage',
                'verbose_name_plural': 'BlogImages',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('url_handle', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('featured_image_url', models.CharField(max_length=255)),
                ('url_handle', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('is_visible', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='app.category')),
            ],
            options={
                'verbose_name': 'BlogPost',
                'verbose_name_plural': 'BlogPosts',
            },
        ),
    ]

# Generated by Django 2.2.5 on 2019-12-10 21:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_auto_20191207_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('semantic_tag', models.CharField(max_length=150)),
                ('data_fields', django.contrib.postgres.fields.jsonb.JSONField(default='')),
                ('post_posttype', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='community.post_type_header')),
            ],
        ),
    ]

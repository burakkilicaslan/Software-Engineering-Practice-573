# Generated by Django 2.2.5 on 2019-12-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_community_header_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='define_post_types',
            name='label_structure',
            field=models.CharField(choices=[('Text', 'Text'), ('BOOL', 'Boolean'), ('IMG', 'Image'), ('Audio', 'Audio'), ('EM', 'E-mail'), ('Video', 'Video'), ('Date', 'Date'), ('Int', 'Number')], max_length=10),
        ),
    ]

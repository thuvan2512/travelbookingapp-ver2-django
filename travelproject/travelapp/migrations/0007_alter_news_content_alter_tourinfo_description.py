# Generated by Django 4.0.3 on 2022-04-30 10:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_alter_news_content_alter_tourinfo_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='tourinfo',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

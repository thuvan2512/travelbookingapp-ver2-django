# Generated by Django 4.0.3 on 2022-07-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0029_alter_newsview_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetour',
            name='image',
            field=models.ImageField(null=True, upload_to='images/tours/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='images/news/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(null=True, upload_to='images/tours/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/users/%Y/%m'),
        ),
    ]

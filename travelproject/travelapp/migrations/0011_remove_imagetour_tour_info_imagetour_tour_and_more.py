# Generated by Django 4.0.3 on 2022-05-02 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0010_typeofpayment_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetour',
            name='tour_info',
        ),
        migrations.AddField(
            model_name='imagetour',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='travelapp.tour'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='payment_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bills', to='travelapp.typeofpayment'),
        ),
    ]
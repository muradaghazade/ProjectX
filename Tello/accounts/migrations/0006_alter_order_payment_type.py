# Generated by Django 3.2.8 on 2021-11-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_order_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('Onlayn kart ilə ödəmə', 'Onlayn kart ilə ödəmə'), ('Qapıda nağd ödəmə', 'Qapıda nağd ödəmə')], max_length=6000),
        ),
    ]

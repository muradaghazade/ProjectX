# Generated by Django 3.2.8 on 2021-11-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Final price'),
            preserve_default=False,
        ),
    ]

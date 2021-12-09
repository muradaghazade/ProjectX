# Generated by Django 3.2.8 on 2021-11-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_adress',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email adress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_home_number',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_number',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer_surname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='message_for_courier',
            field=models.TextField(default='', verbose_name='Message for courier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('Cart', 'Cart'), ('Cash', 'Cash')], default='', max_length=6),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.8 on 2021-10-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='storage',
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='storage_product', to='core.Storage', verbose_name='Color'),
        ),
    ]

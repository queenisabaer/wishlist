# Generated by Django 5.0.6 on 2024-06-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0005_alter_wishlist_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='occassion',
            field=models.IntegerField(choices=[(0, 'Anniversary'), (1, 'Baby Shower'), (2, 'Birthday'), (3, 'Bridal shower'), (4, 'Christmas'), (5, 'Wedding'), (6, 'Celebration')], default=0),
        ),
    ]
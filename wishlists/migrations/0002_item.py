# Generated by Django 5.0.6 on 2024-06-11 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(blank=True, max_length=250)),
                ('item_link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('priority', models.IntegerField(choices=[(0, 'high'), (1, 'medium'), (2, 'low'), (3, 'no-priority')], default=3)),
                ('wish_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='wishlists.wishlist')),
            ],
        ),
    ]

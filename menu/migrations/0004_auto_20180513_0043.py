# Generated by Django 2.0.5 on 2018-05-13 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180512_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='related_items',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_hdr_key', to='menu.Item_hdr'),
        ),
    ]

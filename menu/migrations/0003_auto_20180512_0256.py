# Generated by Django 2.0.5 on 2018-05-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20180511_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_hdr',
            name='item_type',
            field=models.CharField(choices=[('S', 'Snack'), ('D', 'Drink')], default='D', max_length=1),
        ),
    ]

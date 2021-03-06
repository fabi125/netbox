# Generated by Django 3.0.3 on 2020-02-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0099_powerfeed_negative_voltage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]

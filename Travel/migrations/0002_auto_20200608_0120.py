# Generated by Django 3.0.7 on 2020-06-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooking1',
            name='rent_price',
            field=models.CharField(max_length=50),
        ),
    ]
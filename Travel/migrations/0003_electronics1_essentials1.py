# Generated by Django 3.0.7 on 2020-06-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0002_auto_20200608_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='electronics1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('rent_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='essentials1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('rent_price', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 3.1 on 2020-08-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]

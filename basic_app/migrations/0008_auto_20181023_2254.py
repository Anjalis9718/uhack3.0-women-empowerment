# Generated by Django 2.1.1 on 2018-10-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20181023_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

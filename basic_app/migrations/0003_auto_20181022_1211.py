# Generated by Django 2.1.1 on 2018-10-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20181022_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='D_O_B',
            field=models.DateField(),
        ),
    ]
# Generated by Django 2.1.1 on 2018-10-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20181024_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=100)),
                ('DEALS_REGARDING', models.CharField(max_length=200)),
                ('CONTACT_NO', models.CharField(max_length=12)),
                ('EMAIL', models.EmailField(max_length=70)),
            ],
        ),
    ]

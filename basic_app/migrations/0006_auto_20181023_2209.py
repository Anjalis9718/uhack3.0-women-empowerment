# Generated by Django 2.1.1 on 2018-10-23 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='Skills',
            new_name='Extra_Skills',
        ),
    ]

# Generated by Django 2.2 on 2020-10-02 11:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0009_auto_20201002_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='branches',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pune', 'PUNE'), ('Mumbai', 'MUMBAI'), ('Hyd', 'HYDERABAD'), ('Bang', 'BANGALORE')], max_length=50),
        ),
    ]

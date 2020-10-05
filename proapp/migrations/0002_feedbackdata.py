# Generated by Django 2.2 on 2020-10-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=50)),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2023-03-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='seat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='student',
            field=models.CharField(max_length=4, null=True),
        ),
    ]

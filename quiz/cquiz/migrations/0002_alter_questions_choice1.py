# Generated by Django 4.2.4 on 2023-10-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cquiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='choice1',
            field=models.TextField(max_length=1000),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]

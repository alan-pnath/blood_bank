# Generated by Django 4.1.1 on 2022-12-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_blood_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_users',
            name='E_mail',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital_users',
            name='PH_number',
            field=models.CharField(max_length=30),
        ),
    ]

# Generated by Django 4.1.1 on 2022-12-22 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_alter_blood_donor_register_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_donor_register',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

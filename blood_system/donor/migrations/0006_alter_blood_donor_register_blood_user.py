# Generated by Django 4.1.1 on 2022-11-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_alter_blood_donor_register_blood_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_donor_register',
            name='Blood_User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='donor.blood_users'),
        ),
    ]

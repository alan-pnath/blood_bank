# Generated by Django 4.1.1 on 2022-12-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0005_alter_organ_donor_form_id_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organ_donor_form',
            name='Date_Of_Birth',
            field=models.CharField(max_length=10),
        ),
    ]
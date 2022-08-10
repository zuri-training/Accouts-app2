# Generated by Django 4.0.6 on 2022-08-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schreg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='type',
            field=models.CharField(choices=[('CRECHE', 'Creche'), ('NURSERY', 'Nursery'), ('PRIMARY', 'Primary'), ('SECONDARY', 'Secondary'), ('VOCATIONAL', 'Vocational'), ('TECHNICAL', 'Technical')], default='CRECHE', max_length=10),
        ),
    ]
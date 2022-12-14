# Generated by Django 4.0.6 on 2022-08-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_address', models.CharField(max_length=300)),
                ('school_proprietor', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('LGA', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=10)),
                ('file_field', models.FileField(upload_to='')),
                ('type', models.CharField(choices=[('CRECHE', 'Creche'), ('NURSERY', 'Nursery'), ('PRIMARY', 'Primary'), ('SECONDARY', 'Secondary'), ('VOCATIONAL', 'Vocational'), ('TECHNICAL', 'Technical')], default='Creche', max_length=10)),
            ],
        ),
    ]

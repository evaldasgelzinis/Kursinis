# Generated by Django 4.1.7 on 2023-02-26 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool_register', '0006_workplace_employee_date_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]

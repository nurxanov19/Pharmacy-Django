# Generated by Django 5.1.6 on 2025-03-04 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2025, 3, 4)),
        ),
    ]

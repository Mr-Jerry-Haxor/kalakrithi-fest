# Generated by Django 4.1.7 on 2023-02-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_entries_verification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

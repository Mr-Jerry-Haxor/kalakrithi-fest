# Generated by Django 4.1.7 on 2023-02-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='qrhash',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='qrtext',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
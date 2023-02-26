# Generated by Django 4.1.7 on 2023-02-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('registrationnumber', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('campus', models.CharField(max_length=100)),
                ('registrar', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='qrvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrtext', models.CharField(max_length=200)),
                ('qrhash', models.CharField(max_length=300)),
            ],
        ),
    ]

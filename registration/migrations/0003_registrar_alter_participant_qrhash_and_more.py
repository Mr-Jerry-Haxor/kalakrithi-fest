# Generated by Django 4.1.7 on 2023-02-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_participant_qrhash_participant_qrtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='participant',
            name='qrhash',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='participant',
            name='qrtext',
            field=models.CharField(default='', max_length=200),
        ),
    ]

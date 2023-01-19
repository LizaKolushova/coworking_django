# Generated by Django 4.0.5 on 2023-01-18 12:04

import booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False, 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'managed': False, 'verbose_name': 'Бронь', 'verbose_name_plural': 'Брони'},
        ),
        migrations.AlterModelOptions(
            name='historicalauthuser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Пользователь', 'verbose_name_plural': 'historical Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='historicalbooking',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Бронь', 'verbose_name_plural': 'historical Брони'},
        ),
        migrations.AlterModelOptions(
            name='historicalpayment',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Счет', 'verbose_name_plural': 'historical Счета'},
        ),
        migrations.AlterModelOptions(
            name='historicalplace',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Коворкинг', 'verbose_name_plural': 'historical Коворкинги'},
        ),
        migrations.AlterModelOptions(
            name='historicalrate',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Комната', 'verbose_name_plural': 'historical Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'managed': False, 'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'managed': False, 'verbose_name': 'Коворкинг', 'verbose_name_plural': 'Коворкинги'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'managed': False, 'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterField(
            model_name='historicalpayment',
            name='receipt_number',
            field=models.IntegerField(db_column='receipt-number', validators=[booking.models.validate_receipt]),
        ),
    ]

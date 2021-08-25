# Generated by Django 3.1.7 on 2021-08-25 18:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20210715_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycamp',
            name='phone_receiving_2',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=9, null=True, validators=[django.core.validators.RegexValidator('^[-\\s\\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')], verbose_name='Telefon kontaktowy do osoby upoważnionej do odbioru'),
        ),
        migrations.AlterField(
            model_name='daycamp',
            name='phone_receiving_3',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=9, null=True, validators=[django.core.validators.RegexValidator('^[-\\s\\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')], verbose_name='Telefon kontaktowy do osoby upoważnionej do odbioru'),
        ),
        migrations.AlterField(
            model_name='daycamp',
            name='receiving_person_2',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=255, null=True, verbose_name='Imię i nazwisko osoby upoważnionej do dobioru dziecka'),
        ),
        migrations.AlterField(
            model_name='daycamp',
            name='receiving_person_3',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=255, null=True, verbose_name='Imię i nazwisko osoby upoważnionej do dobioru dziecka'),
        ),
        migrations.AlterField(
            model_name='daycamp',
            name='relationship_child_2',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=255, null=True, verbose_name='Relacje z dzieckiem (dziadek, wujek, sąsiadka)'),
        ),
        migrations.AlterField(
            model_name='daycamp',
            name='relationship_child_3',
            field=models.CharField(default='-----', help_text='Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian', max_length=255, null=True, verbose_name='Relacje z dzieckiem (dziadek, wujek, sąsiadka)'),
        ),
    ]
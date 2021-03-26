# Generated by Django 3.1.7 on 2021-03-23 12:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20210321_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=255, verbose_name='Imię i nazwisko rodzica/opiekuna')),
                ('parent_email', models.EmailField(max_length=254, verbose_name='Adres mailowy rodzica/opiekuna')),
                ('child_name', models.CharField(max_length=255, verbose_name='Imię i nazwisko dziecka')),
                ('child_birth_date', models.DateField(verbose_name='Data urodzenia')),
                ('child_pesel', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[-\\s\\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')], verbose_name='PESEL')),
                ('street_address', models.CharField(max_length=254, verbose_name='Adres zamieszkania (ulica, nr domu, nr mieszkania)')),
                ('postal_code', models.CharField(max_length=6, verbose_name='Kod pocztowy')),
                ('city_address', models.CharField(max_length=100, verbose_name='Miejscowość')),
                ('phone_parent_1', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[-\\s\\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')], verbose_name='Telefon kontaktowy nr 1 do rodzica/opiekuna')),
                ('phone_parent_2', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[-\\s\\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')], verbose_name='Telefon kontaktowy nr 2 do rodzica/opiekuna')),
                ('school_name', models.CharField(max_length=255, verbose_name='Nazwa Szkoły')),
                ('school_address', models.CharField(max_length=255, verbose_name='Adres szkoły (ulica, kod pocztowy, miejscowość')),
                ('school_class', models.CharField(max_length=2, verbose_name='Klasa do której dziecko uczęszcza')),
                ('interests_child', models.CharField(max_length=255, verbose_name='Zainteresowania dizecka (wymienić kilka najważniejszych oddzielając przecinkiem')),
                ('data_enrol', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='camp',
            name='child_name',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='city_address',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='interests_child',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='school_address',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='camp',
            name='street_address',
        ),
    ]
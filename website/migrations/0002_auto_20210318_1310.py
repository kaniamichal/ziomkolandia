# Generated by Django 3.1.7 on 2021-03-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kindergarten',
            name='kinder_name',
            field=models.CharField(choices=[('Przedszkole w Debrznie', 'Przedszkole w Debrznie'), ('Przedszkole w Wierzchowie Człuwoskim', 'Przedszkole w Wierzchowie Człuwoskim'), ('Przedszkole Jacka i Agatki w Człuchpwie', 'Przedszkole Jacka i Agatki w Człuchpwie'), ('Przedszkole Bajka w Człuchowie', 'Przedszkole Bajka w Człuchowie'), ('Przedszkole Smyk w Człuchowie', 'Przedszkole Smyk w Człuchowie'), ('Przedszkole Piano w Człuchowie', 'Przedszkole Piano w Człuchowie')], default='Przedszkole w Debrznie', max_length=255),
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='regulations',
            field=models.CharField(choices=[('YES', 'Tak'), ('NO', 'Nie')], default='YES', max_length=3),
        ),
    ]

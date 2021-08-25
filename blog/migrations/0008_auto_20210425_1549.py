# Generated by Django 3.1.7 on 2021-04-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210408_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date_added',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment'),
        ),
    ]
# Generated by Django 3.0.9 on 2020-08-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='test_field',
            field=models.BooleanField(default=True, verbose_name='Тестовое поле'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-10-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_remove_mailing_date_of_first_dispatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='datetime_to_start',
        ),
        migrations.AddField(
            model_name='mailing',
            name='date_of_first_dispatch',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата первой отправки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='client_list',
            field=models.ManyToManyField(help_text='Выберите клиентов для рассылки', related_name='client', to='mailing.client', verbose_name='Клиенты'),
        ),
    ]

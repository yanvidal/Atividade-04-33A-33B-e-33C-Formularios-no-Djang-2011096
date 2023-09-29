# Generated by Django 3.2.13 on 2023-09-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogos',
            old_name='time1',
            new_name='jogos',
        ),
        migrations.RemoveField(
            model_name='jogos',
            name='time2',
        ),
        migrations.AddField(
            model_name='jogos',
            name='placar',
            field=models.CharField(default=5, max_length=10),
            preserve_default=False,
        ),
    ]
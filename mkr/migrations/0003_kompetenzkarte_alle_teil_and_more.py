# Generated by Django 4.0.5 on 2022-06-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkr', '0002_rename_medien_kompetenzkarte_medienkompetenz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kompetenzkarte',
            name='alle_teil',
            field=models.CharField(choices=[('0', 'ist für alle '), ('1', 'Teilgruppe')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='durchf_planung',
            field=models.CharField(choices=[('0', 'wird durchgeführt'), ('1', 'Planung/Umsetzung')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='pflicht_empf',
            field=models.CharField(choices=[('0', 'Pflicht'), ('1', 'Empfehlung')], default='', max_length=1),
            preserve_default=False,
        ),
    ]

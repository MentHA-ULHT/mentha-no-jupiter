# Generated by Django 3.2.3 on 2022-05-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contacto',
            name='mensagem',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='referenciacao',
            field=models.CharField(blank=True, choices=[('ADEB', 'ADEB'), ('ASMAL', 'ASMAL'), ('Elo Social', 'Elo Social'), ('CVP', 'CVP'), ('FamiliarMente', 'FamiliarMente'), ('GIRA', 'GIRA'), ('Outro', 'Outro')], max_length=30),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='assunto',
            field=models.CharField(help_text='Insira a sua mensagem aqui...', max_length=50),
        ),
    ]

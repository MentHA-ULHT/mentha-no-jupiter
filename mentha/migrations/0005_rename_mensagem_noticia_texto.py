# Generated by Django 3.2.3 on 2022-05-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0004_auto_20220511_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='mensagem',
            new_name='texto',
        ),
    ]
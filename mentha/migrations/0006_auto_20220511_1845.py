# Generated by Django 3.2.3 on 2022-05-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0005_rename_mensagem_noticia_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(null=True, upload_to='mentha/noticias/'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='url',
            field=models.URLField(null=True),
        ),
    ]

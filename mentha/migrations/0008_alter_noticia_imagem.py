# Generated by Django 3.2.3 on 2022-05-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0007_alter_noticia_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='mentha/noticias/'),
        ),
    ]

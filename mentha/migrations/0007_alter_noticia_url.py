# Generated by Django 3.2.3 on 2022-05-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0006_auto_20220511_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2 on 2021-05-04 01:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listaApp', '0007_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Img',
            new_name='ImagemUser',
        ),
    ]

# Generated by Django 3.2 on 2021-05-04 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaApp', '0005_auto_20210503_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='imge',
        ),
    ]
# Generated by Django 3.2 on 2021-05-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaApp', '0011_alter_imagemuser_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemuser',
            name='imagem',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='data_criacao',
            field=models.DateField(default='2021-05-05'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='data_termino',
            field=models.DateField(default='2021-05-05'),
        ),
    ]

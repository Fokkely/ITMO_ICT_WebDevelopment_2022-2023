# Generated by Django 4.1.2 on 2022-12-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
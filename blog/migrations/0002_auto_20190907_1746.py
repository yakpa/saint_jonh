# Generated by Django 2.2.2 on 2019-09-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication',
            field=models.DateField(verbose_name='date de publication'),
        ),
    ]

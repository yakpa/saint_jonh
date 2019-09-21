# Generated by Django 2.2.2 on 2019-09-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]

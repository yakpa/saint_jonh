# Generated by Django 2.2.2 on 2019-09-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

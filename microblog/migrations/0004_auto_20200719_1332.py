# Generated by Django 2.2.14 on 2020-07-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0003_auto_20200718_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Treść'),
        ),
    ]

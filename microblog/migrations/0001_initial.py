# Generated by Django 2.2.14 on 2020-10-11 21:21

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonim', max_length=80, verbose_name='Autor')),
                ('text', models.TextField(max_length=500, verbose_name='Treść')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('update', models.DateTimeField(blank=True, null=True, verbose_name='Data modyfikacji')),
                ('active', models.BooleanField(default=True, verbose_name='Aktywny')),
            ],
            options={
                'verbose_name': 'Komentarz',
                'verbose_name_plural': 'Komentarze',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=50, verbose_name='Tagi')),
                ('title', models.CharField(max_length=100, verbose_name='Tytuł')),
                ('short', models.TextField(max_length=1000, verbose_name='Skrót')),
                ('contents', ckeditor.fields.RichTextField(blank=True, max_length=100000000, null=True, verbose_name='Pełna treść')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data utworzenia')),
                ('publication_date', models.DateTimeField(blank=True, null=True, verbose_name='Data publikacji')),
                ('category', models.ManyToManyField(blank=True, to='microblog.BlogCategory', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posty',
            },
        ),
    ]

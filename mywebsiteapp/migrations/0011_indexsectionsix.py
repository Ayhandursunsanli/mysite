# Generated by Django 4.2.3 on 2023-11-28 12:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0010_indexsectionfive_firstsubsectionfive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexsectionsix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Anasayfa - Section-6 (Seo Alanı)',
                'verbose_name_plural': 'Anasayfa - Section-6 (Seo Alanı)',
            },
        ),
    ]

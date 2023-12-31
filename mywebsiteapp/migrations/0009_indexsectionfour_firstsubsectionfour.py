# Generated by Django 4.2.3 on 2023-11-28 10:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0008_indexsectionthree_alter_headercarousel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexsectionfour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Anasayfa - Section-4',
                'verbose_name_plural': 'Anasayfa Section-4',
            },
        ),
        migrations.CreateModel(
            name='FirstSubSectionFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('sue', ckeditor.fields.RichTextField()),
                ('analysis', ckeditor.fields.RichTextField()),
                ('design', ckeditor.fields.RichTextField()),
                ('coding', ckeditor.fields.RichTextField()),
                ('testing_release', ckeditor.fields.RichTextField()),
                ('maintenance_support', ckeditor.fields.RichTextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywebsiteapp.indexsectionfour')),
            ],
        ),
    ]

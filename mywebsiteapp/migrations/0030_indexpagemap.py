# Generated by Django 4.2.3 on 2023-12-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0029_footer_description_en_footer_description_tr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexpagemap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('title_tr', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('href_id', models.CharField(max_length=250, null=True)),
                ('href_title', models.CharField(max_length=250, null=True)),
                ('href_title_tr', models.CharField(max_length=250, null=True)),
                ('href_title_en', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Anasayfa - Sayfa Haritası',
                'verbose_name_plural': 'Anasayfa - Sayfa Haritası',
            },
        ),
    ]

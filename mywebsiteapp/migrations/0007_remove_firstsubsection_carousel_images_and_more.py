# Generated by Django 4.2.3 on 2023-11-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0006_remove_firstsubsection_carousel_image_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstsubsection',
            name='carousel_images',
        ),
        migrations.AddField(
            model_name='firstsubsection',
            name='carousel_image_1',
            field=models.ImageField(null=True, upload_to='indexsectiononecarousel_images/'),
        ),
        migrations.AddField(
            model_name='firstsubsection',
            name='carousel_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='indexsectiononecarousel_images/'),
        ),
        migrations.AddField(
            model_name='firstsubsection',
            name='carousel_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='indexsectiononecarousel_images/'),
        ),
        migrations.AddField(
            model_name='firstsubsection',
            name='carousel_image_4',
            field=models.ImageField(blank=True, null=True, upload_to='indexsectiononecarousel_images/'),
        ),
    ]

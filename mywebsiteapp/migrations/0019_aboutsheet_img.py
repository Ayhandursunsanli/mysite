# Generated by Django 4.2.3 on 2023-11-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0018_aboutsheet_myskills_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsheet',
            name='img',
            field=models.ImageField(null=True, upload_to='about_images/'),
        ),
    ]

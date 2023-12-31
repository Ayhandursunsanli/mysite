# Generated by Django 4.2.3 on 2023-12-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0034_alter_projectssheet_breadcrumboneurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcard',
            name='buttonText_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='projectcard',
            name='buttonText_tr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='projectcard',
            name='site_title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectcard',
            name='site_title_tr',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

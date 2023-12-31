# Generated by Django 4.2.3 on 2023-11-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0013_footer_footersubsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='footersubsection',
            name='socialmedia',
            field=models.CharField(max_length=50, null=True, verbose_name='Sosyal Medya İcon Uzantısı (Örn: fa fa-github)'),
        ),
        migrations.AddField(
            model_name='footersubsection',
            name='socialmedia_link',
            field=models.URLField(null=True, verbose_name='Sosyal Medya İtemi Linki'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='footer_images/'),
        ),
        migrations.AlterField(
            model_name='footersubsection',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Menü İtemi'),
        ),
        migrations.AlterField(
            model_name='footersubsection',
            name='url',
            field=models.CharField(max_length=500, null=True, verbose_name='Menü İtemi Linki'),
        ),
    ]

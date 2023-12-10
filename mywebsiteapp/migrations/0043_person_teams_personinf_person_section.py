# Generated by Django 4.2.3 on 2023-12-10 15:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0042_projectcard_site_about_projectcard_site_about_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('name_tr', models.CharField(max_length=250, null=True)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('job', models.CharField(max_length=250, null=True)),
                ('job_tr', models.CharField(max_length=250, null=True)),
                ('job_en', models.CharField(max_length=250, null=True)),
                ('img', models.ImageField(null=True, upload_to='person_images/')),
                ('social_icon1', models.CharField(blank=True, max_length=250, null=True)),
                ('social_url1', models.URLField(blank=True, null=True)),
                ('social_icon2', models.CharField(blank=True, max_length=250, null=True)),
                ('social_url2', models.URLField(blank=True, null=True)),
                ('social_icon3', models.CharField(blank=True, max_length=250, null=True)),
                ('social_url3', models.URLField(blank=True, null=True)),
                ('social_icon4', models.CharField(blank=True, max_length=250, null=True)),
                ('social_url4', models.URLField(blank=True, null=True)),
                ('navLink1', models.CharField(max_length=250, null=True)),
                ('navLink_title1', models.CharField(max_length=250, null=True)),
                ('navLink_title1_tr', models.CharField(max_length=250, null=True)),
                ('navLink_title1_en', models.CharField(max_length=250, null=True)),
                ('navLink_about1', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about1_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about1_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink2', models.CharField(max_length=250, null=True)),
                ('navLink_title2', models.CharField(max_length=250, null=True)),
                ('navLink_title2_tr', models.CharField(max_length=250, null=True)),
                ('navLink_title2_en', models.CharField(max_length=250, null=True)),
                ('navLink_about2', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about2_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about2_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink3', models.CharField(max_length=250, null=True)),
                ('navLink_title3', models.CharField(max_length=250, null=True)),
                ('navLink_title3_tr', models.CharField(max_length=250, null=True)),
                ('navLink_title3_en', models.CharField(max_length=250, null=True)),
                ('navLink_about3', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about3_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about3_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink4', models.CharField(max_length=250, null=True)),
                ('navLink_title4', models.CharField(max_length=250, null=True)),
                ('navLink_title4_tr', models.CharField(max_length=250, null=True)),
                ('navLink_title4_en', models.CharField(max_length=250, null=True)),
                ('navLink_about4', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about4_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about4_en', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breadcrumbOne', models.CharField(max_length=250, null=True)),
                ('breadcrumbOne_tr', models.CharField(max_length=250, null=True)),
                ('breadcrumbOne_en', models.CharField(max_length=250, null=True)),
                ('breadcrumbOneUrl', models.CharField(max_length=250, null=True)),
                ('breadcrumbTwo', models.CharField(max_length=250, null=True)),
                ('breadcrumbTwo_tr', models.CharField(max_length=250, null=True)),
                ('breadcrumbTwo_en', models.CharField(max_length=250, null=True)),
                ('headTitle', models.CharField(max_length=250, null=True)),
                ('headTitle_tr', models.CharField(max_length=250, null=True)),
                ('headTitle_en', models.CharField(max_length=250, null=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('title_tr', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('about', ckeditor.fields.RichTextField(null=True)),
                ('about_tr', ckeditor.fields.RichTextField(null=True)),
                ('about_en', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navLink_about', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_about_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink_cv_header', models.CharField(max_length=250, null=True)),
                ('navLink_cv_header_tr', models.CharField(max_length=250, null=True)),
                ('navLink_cv_header_en', models.CharField(max_length=250, null=True)),
                ('navLink_cv_year', models.CharField(max_length=250, null=True)),
                ('navLink_cv_job', models.CharField(max_length=250, null=True)),
                ('navLink_cv_job_tr', models.CharField(max_length=250, null=True)),
                ('navLink_cv_job_en', models.CharField(max_length=250, null=True)),
                ('navLink_cv_company', models.CharField(max_length=250, null=True)),
                ('navLink_cv_company_tr', models.CharField(max_length=250, null=True)),
                ('navLink_cv_company_en', models.CharField(max_length=250, null=True)),
                ('navLink_sill_about', ckeditor.fields.RichTextField(null=True)),
                ('navLink_sill_about_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_sill_about_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink_skill_img', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img2', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img3', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img4', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img5', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img6', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img7', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img8', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_skill_img9', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_cer_about', ckeditor.fields.RichTextField(null=True)),
                ('navLink_cer_about_tr', ckeditor.fields.RichTextField(null=True)),
                ('navLink_cer_about_en', ckeditor.fields.RichTextField(null=True)),
                ('navLink_cer_img', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_cer_img2', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_cer_img3', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('navLink_cer_img4', models.ImageField(blank=True, null=True, upload_to='person_images/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywebsiteapp.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mywebsiteapp.teams'),
        ),
    ]

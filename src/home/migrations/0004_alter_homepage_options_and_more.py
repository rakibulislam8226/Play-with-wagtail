# Generated by Django 5.0.1 on 2024-02-03 07:38

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_subtitle_homepage_banner_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]

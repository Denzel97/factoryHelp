# Generated by Django 5.0 on 2023-12-31 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_company_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
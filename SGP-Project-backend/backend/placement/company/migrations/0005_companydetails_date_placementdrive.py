# Generated by Django 5.0.6 on 2025-02-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_remove_companydetails_date_placementdrive'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='date_placementdrive',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_upload_records_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='time_limit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

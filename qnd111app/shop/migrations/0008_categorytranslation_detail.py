# Generated by Django 3.2.15 on 2022-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_categorytranslation_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytranslation',
            name='detail',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]

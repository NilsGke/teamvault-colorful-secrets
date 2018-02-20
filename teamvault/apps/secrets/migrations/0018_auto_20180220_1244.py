# Generated by Django 2.0 on 2018-02-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0017_auto_20180220_1115'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='secretrevision',
            unique_together={('plaintext_data_sha256', 'secret')},
        ),
        migrations.RemoveField(
            model_name='secretrevision',
            name='encrypted_data_sha256',
        ),
    ]

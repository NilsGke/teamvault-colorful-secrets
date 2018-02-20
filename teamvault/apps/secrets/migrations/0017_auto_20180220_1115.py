# Generated by Django 2.0 on 2018-02-20 11:15

from django.db import migrations


def remove_duplicate_srevs(apps, schema_editor):
    LogEntry = apps.get_model('audit', 'LogEntry')
    Secret = apps.get_model('secrets', 'Secret')
    SecretRevision = apps.get_model('secrets', 'SecretRevision')
    for secret in Secret.objects.all():
        revisions = SecretRevision.objects.filter(secret=secret).order_by('-id')
        hashes_to_revisions = {}
        for revision in revisions:
            if revision.plaintext_data_sha256 in hashes_to_revisions:
                correct_revision = hashes_to_revisions[revision.plaintext_data_sha256]
                assert revision != revision.secret.current_revision
                for log_entry in LogEntry.objects.filter(secret_revision=revision):
                    log_entry.secret_revision = correct_revision
                    log_entry.save()
                correct_revision.accessed_by.add(*list(revision.accessed_by.all()))
                revision.delete()
            else:
                hashes_to_revisions[revision.plaintext_data_sha256] = revision


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0016_auto_20180220_1053'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_srevs),
    ]

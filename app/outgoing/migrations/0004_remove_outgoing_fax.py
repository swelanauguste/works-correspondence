# Generated by Django 5.0.4 on 2024-04-29 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outgoing', '0003_alter_outgoing_fax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outgoing',
            name='fax',
        ),
    ]

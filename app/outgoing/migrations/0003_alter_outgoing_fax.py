# Generated by Django 5.0.4 on 2024-04-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outgoing', '0002_alter_outgoing_fax_alter_outgoing_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing',
            name='fax',
            field=models.BooleanField(default=False),
        ),
    ]

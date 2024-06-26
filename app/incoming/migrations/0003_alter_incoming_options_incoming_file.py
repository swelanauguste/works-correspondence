# Generated by Django 5.0.4 on 2024-04-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0002_action_rename_r_from_incoming_rfrom_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incoming',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='incoming',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='incoming/files/'),
        ),
    ]

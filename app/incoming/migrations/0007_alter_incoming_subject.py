# Generated by Django 5.0.4 on 2024-04-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0006_alter_incoming_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0009_remove_incoming_date_alter_incoming_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

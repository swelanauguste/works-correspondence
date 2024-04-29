# Generated by Django 5.0.4 on 2024-04-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0003_alter_incoming_options_incoming_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming',
            name='action',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='incoming',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Action',
        ),
    ]
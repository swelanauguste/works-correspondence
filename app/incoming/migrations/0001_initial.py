# Generated by Django 5.0.4 on 2024-04-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('received', models.DateField(blank=True, null=True)),
                ('dated', models.DateField(blank=True, null=True)),
                ('r_from', models.CharField(max_length=100, verbose_name='from')),
                ('to', models.CharField(blank=True, max_length=100, null=True)),
                ('cc', models.CharField(blank=True, max_length=100, null=True)),
                ('action', models.CharField(blank=True, max_length=100, null=True)),
                ('forward', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
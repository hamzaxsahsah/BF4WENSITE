# Generated by Django 4.2.4 on 2023-08-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4aservice_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('service_description', models.CharField(max_length=500)),
                ('bootstrap_icon', models.CharField(max_length=50)),
            ],
        ),
    ]

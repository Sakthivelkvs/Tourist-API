# Generated by Django 5.0.8 on 2024-10-31 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('conf_password', models.CharField(max_length=200)),
            ],
        ),
    ]

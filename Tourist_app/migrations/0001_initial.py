# Generated by Django 5.0.8 on 2024-10-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_Name', models.CharField(max_length=200)),
                ('Weather', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('Google_Map_Link', models.URLField(max_length=500)),
                ('Image', models.ImageField(upload_to='tourist/')),
                ('Description', models.CharField(max_length=2000)),
            ],
        ),
    ]

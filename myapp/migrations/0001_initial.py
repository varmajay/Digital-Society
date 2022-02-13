# Generated by Django 4.0.2 on 2022-02-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('pic', models.FileField(blank=True, default='pic.png', null=True, upload_to='profile')),
                ('verify', models.BooleanField(default=False)),
            ],
        ),
    ]
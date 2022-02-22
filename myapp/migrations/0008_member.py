# Generated by Django 4.0.2 on 2022-02-22 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_house_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('doc', models.CharField(max_length=20)),
                ('doc_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('verify', models.BooleanField(default=False)),
                ('pic', models.FileField(default='member-pic.png', upload_to='member_pic')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.house')),
            ],
        ),
    ]

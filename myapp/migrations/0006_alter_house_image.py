# Generated by Django 4.0.2 on 2022-02-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.FileField(default='IMG20201120175428.jpg', upload_to='house-image'),
        ),
    ]

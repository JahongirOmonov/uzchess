# Generated by Django 5.0.2 on 2024-02-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_delete_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
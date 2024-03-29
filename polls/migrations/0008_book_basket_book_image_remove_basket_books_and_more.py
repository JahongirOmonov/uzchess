# Generated by Django 5.0.2 on 2024-02-14 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_book_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='basket',
            field=models.ManyToManyField(through='polls.Basket', to='polls.user'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='basket',
            name='books',
        ),
        migrations.AddField(
            model_name='basket',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='polls.book'),
            preserve_default=False,
        ),
    ]

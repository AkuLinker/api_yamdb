# Generated by Django 2.2.16 on 2021-11-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211111_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, default=1234, max_length=20),
            preserve_default=False,
        ),
    ]

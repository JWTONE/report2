# Generated by Django 4.2 on 2024-04-18 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_delete_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1 on 2024-09-11 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyapi', '0009_alter_spotifytoken_token_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='token_expiry',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 4, 25, 3, 824025, tzinfo=datetime.timezone.utc)),
        ),
    ]
# Generated by Django 3.0.2 on 2020-01-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uper', '0003_auto_20200129_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.3 on 2020-08-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_reply_to_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='to_reply',
            field=models.IntegerField(default=0),
        ),
    ]

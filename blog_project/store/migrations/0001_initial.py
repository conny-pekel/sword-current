# Generated by Django 3.0.3 on 2020-07-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('discription', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-17 18:56

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
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True)),
                ('stock', models.IntegerField(blank=True)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]

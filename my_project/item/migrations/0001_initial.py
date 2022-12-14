# Generated by Django 4.1.1 on 2022-10-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('visible', models.BooleanField()),
                ('price', models.FloatField()),
                ('desciption', models.CharField(max_length=255)),
            ],
        ),
    ]

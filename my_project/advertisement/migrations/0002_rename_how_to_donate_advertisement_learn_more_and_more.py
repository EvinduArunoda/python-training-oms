# Generated by Django 4.1.1 on 2022-10-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='how_to_donate',
            new_name='learn_more',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='bg_color',
            field=models.CharField(default='red', max_length=30),
            preserve_default=False,
        ),
    ]
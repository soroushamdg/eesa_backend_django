# Generated by Django 2.2.2 on 2019-07-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eesa_main', '0004_auto_20190708_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eesa_information',
            name='email',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='eesa_information',
            name='instagram',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='eesa_information',
            name='telegram',
            field=models.CharField(default=None, max_length=40),
        ),
    ]

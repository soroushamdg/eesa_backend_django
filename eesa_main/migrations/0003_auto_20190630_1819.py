# Generated by Django 2.2.2 on 2019-06-30 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eesa_main', '0002_auto_20190630_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eesa_team_member',
            old_name='profile_image',
            new_name='image',
        ),
    ]
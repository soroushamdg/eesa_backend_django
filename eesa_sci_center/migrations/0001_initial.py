# Generated by Django 2.2.2 on 2019-07-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scicenter_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Science Center Category',
                'verbose_name_plural': 'Science Center Categories',
            },
        ),
        migrations.CreateModel(
            name='scicenter_writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Science Center writer',
                'verbose_name_plural': 'Science Center writers',
            },
        ),
        migrations.CreateModel(
            name='scicenter_tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('issue_date', models.DateField(auto_now=True)),
                ('pages', models.CharField(blank=True, max_length=4, null=True)),
                ('is_document_url', models.BooleanField()),
                ('document_file', models.FileField(blank=True, null=True, upload_to='scicenter/documents/07/10/2019/14/46/18')),
                ('document_url', models.URLField(blank=True, null=True)),
                ('category', models.ManyToManyField(max_length=5, related_name='scicenter_tutorial_category', to='eesa_sci_center.scicenter_category')),
                ('writer', models.ManyToManyField(max_length=2, related_name='scicenter_tutorial_writer', to='eesa_sci_center.scicenter_writer')),
            ],
        ),
        migrations.CreateModel(
            name='scicenter_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('issue_date', models.DateField(auto_now=True)),
                ('pages', models.CharField(blank=True, max_length=4, null=True)),
                ('is_document_url', models.BooleanField()),
                ('document_file', models.FileField(blank=True, null=True, upload_to='scicenter/documents/07/10/2019/14/46/18')),
                ('document_url', models.URLField(blank=True, null=True)),
                ('category', models.ManyToManyField(max_length=5, related_name='scicenter_project_category', to='eesa_sci_center.scicenter_category')),
                ('writer', models.ManyToManyField(max_length=2, related_name='scicenter_project_writer', to='eesa_sci_center.scicenter_writer')),
            ],
        ),
        migrations.CreateModel(
            name='scicenter_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('issue_date', models.DateField(auto_now=True)),
                ('pages', models.CharField(blank=True, max_length=4, null=True)),
                ('is_document_url', models.BooleanField()),
                ('document_file', models.FileField(blank=True, null=True, upload_to='scicenter/documents/07/10/2019/14/46/18')),
                ('document_url', models.URLField(blank=True, null=True)),
                ('category', models.ManyToManyField(max_length=5, related_name='scicenter_document_category', to='eesa_sci_center.scicenter_category')),
                ('writer', models.ManyToManyField(max_length=2, related_name='scicenter_document_writer', to='eesa_sci_center.scicenter_writer')),
            ],
        ),
    ]
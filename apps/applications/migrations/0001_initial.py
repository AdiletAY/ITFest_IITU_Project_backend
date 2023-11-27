# Generated by Django 4.2.7 on 2023-11-27 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('need_correction', 'Need Correction')], default='sent', max_length=50)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('check_date', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Application Category',
                'verbose_name_plural': 'Application Categories',
            },
        ),
        migrations.CreateModel(
            name='ApplicationPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Period name')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Application Period',
                'verbose_name_plural': 'Application Periods',
            },
        ),
        migrations.CreateModel(
            name='ApplicationCategoryDocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_necessary', models.BooleanField(default=False)),
                ('application_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.applicationcategory', verbose_name='Application Category')),
            ],
            options={
                'verbose_name': 'Document Type',
                'verbose_name_plural': 'Document Types',
            },
        ),
    ]
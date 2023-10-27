# Generated by Django 4.2.2 on 2023-09-21 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Caledon_Reno_Work_Hours', '0005_rename_gc_rate_10_mark_up_job_gc_rate_10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estimate',
            old_name='Blueprint_and_Images',
            new_name='Blueprints_and_Images',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='Phone_Number',
        ),
        migrations.AddField(
            model_name='estimate',
            name='Address',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estimate',
            name='City',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estimate',
            name='Company',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estimate',
            name='Phone',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estimate',
            name='Zip_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estimate',
            name='First_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='Last_Name',
            field=models.CharField(max_length=100),
        ),
    ]

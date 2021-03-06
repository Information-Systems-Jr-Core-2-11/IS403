# Generated by Django 3.1.1 on 2020-12-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=320),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_benefits',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_requirements',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='relocation_package',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='school_experience',
            name='description',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='school_experience',
            name='school_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='experience_description',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='work_experience',
            name='job_title',
            field=models.CharField(max_length=200),
        ),
    ]

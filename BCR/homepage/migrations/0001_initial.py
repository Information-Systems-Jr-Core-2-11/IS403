# Generated by Django 3.1.1 on 2020-12-07 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('desired_title', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('video_link', models.URLField()),
                ('resume_upload', models.FileField(upload_to='')),
                ('seeking_work', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Application_Status',
            fields=[
                ('application_status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.CharField(max_length=8000)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('video_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Experience',
            fields=[
                ('work_exp_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('experience_description', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='School_Experience',
            fields=[
                ('school_exp_id', models.AutoField(primary_key=True, serialize=False)),
                ('major', models.CharField(max_length=50)),
                ('minor', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=50)),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('apply_startDate', models.DateField()),
                ('apply_endDate', models.DateField()),
                ('job_startDate', models.DateField()),
                ('job_location', models.CharField(max_length=50)),
                ('job_description', models.CharField(max_length=50)),
                ('job_requirements', models.CharField(max_length=50)),
                ('relocation_package', models.CharField(max_length=200)),
                ('job_benefits', models.CharField(max_length=500)),
                ('Job_filled', models.BooleanField()),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.IntegerField()),
                ('required', models.BooleanField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.job')),
                ('skill_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.skill')),
            ],
            options={
                'unique_together': {('skill_name', 'job_id')},
            },
        ),
        migrations.CreateModel(
            name='Job_Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_date', models.DateField()),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.applicant')),
            ],
            options={
                'unique_together': {('job_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='Job_Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField()),
                ('application_status_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.application_status')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.applicant')),
            ],
            options={
                'unique_together': {('job_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='Applicant_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.IntegerField()),
                ('skill_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.skill')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homepage.applicant')),
            ],
            options={
                'unique_together': {('skill_name', 'user_id')},
            },
        ),
    ]

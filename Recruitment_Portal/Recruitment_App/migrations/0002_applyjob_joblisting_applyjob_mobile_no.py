# Generated by Django 4.0.8 on 2023-06-06 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='joblisting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Recruitment_App.joblisting'),
        ),
        migrations.AddField(
            model_name='applyjob',
            name='mobile_no',
            field=models.BigIntegerField(null=True),
        ),
    ]

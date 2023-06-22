# Generated by Django 4.0.8 on 2023-06-07 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruitment_App', '0003_remove_applyjob_file_applyjob_coverletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.8 on 2023-06-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_App', '0004_applyjob_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='maximum_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='minimum_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.IntegerField()),
            ],
        ),
    ]

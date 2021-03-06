# Generated by Django 2.2.2 on 2019-06-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation_code', models.CharField(max_length=11)),
                ('phone_number', models.CharField(max_length=11)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_day', models.DateTimeField()),
                ('address', models.CharField(max_length=120)),
                ('sex', models.CharField(choices=[('MR', 'Mr.'), ('MS', 'Ms.')], max_length=3)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-09-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Re_password', models.CharField(max_length=20)),
                ('Contact', models.BigIntegerField(max_length=15)),
            ],
        ),
    ]

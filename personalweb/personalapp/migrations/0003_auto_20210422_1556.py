# Generated by Django 3.2 on 2021-04-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalapp', '0002_auto_20210421_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='contactme',
        ),
    ]

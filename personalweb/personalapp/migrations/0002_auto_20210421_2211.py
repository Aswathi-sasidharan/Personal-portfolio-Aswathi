# Generated by Django 3.2 on 2021-04-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='text',
        ),
    ]

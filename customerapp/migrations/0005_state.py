# Generated by Django 3.1.3 on 2020-12-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0004_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
    ]
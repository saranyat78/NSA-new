# Generated by Django 2.1.7 on 2020-04-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigDiff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device_1', models.CharField(default='', editable=False, max_length=10)),
                ('Device_2', models.CharField(max_length=200)),
            ],
        ),
    ]

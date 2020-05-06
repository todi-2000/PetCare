# Generated by Django 3.0.6 on 2020-05-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
